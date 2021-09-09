import pandas as pd
import numpy as np
import streamlit as st
import operator
import base64
import warnings
warnings.filterwarnings("ignore")

def main():

	def _max_width_():
	    max_width_str = f"max-width: 2000px;"
	    st.markdown(
	        f"""
	    <style>
	    .reportview-container .main .block-container{{
	        {max_width_str}
	    }}
	    </style>    
	    """,
	        unsafe_allow_html=True,
	    )

	def load_data():
		data = pd.read_csv("./Final_Data.csv")
		return data

	df = load_data()

	df.drop('Unnamed: 0',axis = 1,inplace = True)

	arr1 = df.columns.values
	main_list = arr1.ravel().tolist()

	list_quarter = ['201312','201403','201406','201409','201412','201503','201506','201509','201512','201603','201606','201609','201612','201703','201706',
                '201709','201712','201803','201806','201809','201812','201903','201906','201909','201912','202003','202006','202009','202012','202103']

	list_cols = ['Price_','no.of.shareholder.below.1.lakh.nominal.capital_','total.promoter.holding.in','total.institutional.holding.in',
	             'MF.holding.in','insurance.companies.holding.in','AIF.holding.in','FPI_Holding_','Pension.Fund.holding.in',
	             'total.non.institutional.holding.in','retail.shareholder.in','HNI.holding.in']

	col_list = ['Quarter','Price','No of Shareholders below 1 lakh Nominal Capital','Promoter Holding %','Institutional Holding %',
				'Mutual Fund Holding %','Insurance Companies Holding %','AIF Holding %','FPI Holding %','Pension Fund Holding %',
				'Non Institutional Holding %','Retail Shareholder %','HNI Holding %']

	list_scrip = df['name.of.the.scrip'].tolist()

	df.set_index('name.of.the.scrip', inplace=True)

	def get_data(scrip):
	    df_scrip = df.loc[[scrip]]

	    df_converted = pd.DataFrame({'Quarter':list_quarter})

	    for i in list_cols:
	        list1 = []
	        for j in main_list:
	            if(i in j):
	                list1.append(j)

	        list2 = []
	        for p in list1:
	            x = df_scrip.iloc[0][p]
	            list2.append(x)
	            df_converted[i] = pd.Series(list2)

	    df_converted.columns = col_list
	    
	    return df_converted

	def get_file(df):

			csv = df1.to_csv(index = False).encode()
			b64 = base64.b64encode(csv).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="Quarterly Data ({scrip}).csv" target="_blank">Download CSV File</a>'
			st.markdown(href, unsafe_allow_html=True)

	_max_width_()

	st.title("Quarterly Data")

	scrip = st.selectbox("Select Scrip",list_scrip)

	st.subheader(scrip)

	df1 = get_data(scrip)
	df1.index += 1
	
	if st.button("Get CSV"):
		get_file(df1)

	st.table(df1)

if __name__ == '__main__':
	main()
