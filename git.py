import pandas as pd
import numpy as np
import streamlit as st
import operator
import base64
import warnings
warnings.filterwarnings("ignore")

def main():

	def load_data():
		data = pd.read_csv("./Final_Data_Updated.csv")
		return data

	df = load_data()

	arr1 = df.columns.values
	main_list = arr1.ravel().tolist()

	col_dict = {'Price (End Quarter)':'Price_',
				'Quarterly Price Change %':'Price_',
            	'Retail Shareholder Change %':'no.of.shareholder.below.1.lakh.nominal.capital_',
            	'Promoter Holding Change':'total.promoter.holding.in',
            	'Institutional Holding Change':'total.institutional.holding.in',
            	'Mutual Fund Holding Change':'MF.holding.in',
            	'Insurance Companies Holding Change':'insurance.companies.holding.in',
            	'AIF Holding Change':'AIF.holding.in',
            	'FPI Holding Change':'FPI_Holding_',
            	'Pension Fund Holding Change':'Pension.Fund.holding.in',
            	'Total Non Institutional Holding Change':'total.non.institutional.holding.in',
            	'Retail Shareholder Change':'retail.shareholder.in',
            	'HNI Holding Change':'HNI.holding.in'}

	col_list = []

	def get_list(x):
		for i in main_list:
		    if (col_dict.get(x) in i):
		        col_list.append(i)

		return col_list

	list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

	st.title("Scanner")

	ft_select = st.sidebar.multiselect("Functionality",("Price (End Quarter)","Quarterly Price Change %","Retail Shareholder Change %","Promoter Holding Change",
									   "Institutional Holding Change","Mutual Fund Holding Change","Insurance Companies Holding Change",
									   "AIF Holding Change","FPI Holding Change","Pension Fund Holding Change",
									   "Total Non Institutional Holding Change","Retail Shareholder Change","HNI Holding Change"))

	Q1 = st.sidebar.selectbox("Enter Start Quarter",('201312','201403','201406','201409','201412','201503','201506','201509','201512','201603','201606','201609','201612',
						     '201703','201706','201709','201712','201803','201806','201809','201812','201903','201906','201909','201912','202003',
						     '202006','202009','202012','202103'),key = 'quarter2')
	Q2 = st.sidebar.selectbox("Enter End Quarter",('201312','201403','201406','201409','201412','201503','201506','201509','201512','201603','201606','201609','201612',
						     '201703','201706','201709','201712','201803','201806','201809','201812','201903','201906','201909','201912','202003',
						     '202006','202009','202012','202103'),key = 'quarter1')

	def get_Q1(Q1):

		for x in ft_select:

			if x == 'Quarterly Price Change %':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						price1 = col
						list2[0] = price1

			if x == 'Retail Shareholder Change %':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						rsc1 = col
						list2[2] = rsc1

			if x == 'Promoter Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						tph1 = col
						list2[4] = tph1

			if x == 'Institutional Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						ih1 = col
						list2[6] = ih1

			if x == 'Mutual Fund Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						mfh1 = col
						list2[8] = mfh1

			if x == 'Insurance Companies Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						ich1 = col
						list2[10] = ich1

			if x == 'AIF Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						ah1 = col
						list2[12] = ah1

			if x == 'FPI Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						fhc1 = col
						list2[22] = fhc1

			if x == 'Pension Fund Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						pfh1 = col
						list2[14] = pfh1

			if x == 'Total Non Institutional Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						tnh1 = col
						list2[16] = tnh1

			if x == 'Retail Shareholder Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						rc1 = col
						list2[18] = rc1

			if x == 'HNI Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q1 in col:
						hh1 = col
						list2[20] = hh1

	def get_Q2(Q2):

		for x in ft_select:

			if x == 'Price (End Quarter)':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						p2 = col
						list2[1] = p2
			
			if x == 'Quarterly Price Change %':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						price2 = col
						list2[1] = price2

			if x == 'Retail Shareholder Change %':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						rsc2 = col
						list2[3] = rsc2

			if x == 'Promoter Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						tph2 = col
						list2[5] = tph2

			if x == 'Institutional Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						ih2 = col
						list2[7] = ih2

			if x == 'Mutual Fund Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						mfh2 = col
						list2[9] = mfh2

			if x == 'Insurance Companies Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						ich2 = col
						list2[11] = ich2

			if x == 'AIF Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						ah2 = col
						list2[13] = ah2

			if x == 'FPI Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						fhc2 = col
						list2[23] = fhc2

			if x == 'Pension Fund Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						pfh2 = col
						list2[15] = pfh2

			if x == 'Total Non Institutional Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						tnh2 = col
						list2[17] = tnh2

			if x == 'Retail Shareholder Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						rc2 = col
						list2[19] = rc2

			if x == 'HNI Holding Change':
				list1 = get_list(x)
				for col in list1:
					if Q2 in col:
						hh2 = col
						list2[21] = hh2

	get_Q1(Q1)
	get_Q2(Q2)
	
	if float(Q1) > float(Q2):
		st.error("Invalid Input : Start Quarter greater than End Quarter")

	else:
		def multi_fun(y = []):

			df1 = df

			my_list1 = ['name.of.the.scrip']

			for x in y:

				if x == 'Price (End Quarter)':
					df1[x] = df1[list2[1]].round(2)
					my_list1.append(x)

				if x == 'Quarterly Price Change %':
					df1[x] = (((df1[list2[1]]-df1[list2[0]])/df1[list2[0]])*100).round(2)
					my_list1.append(x)

				if x == 'Retail Shareholder Change %':
					df1[x] = (((df1[list2[3]]-df1[list2[2]])/df1[list2[2]])*100).round(2)
					my_list1.append(x)

				if x == 'Promoter Holding Change':
					df1[x] = (df1[list2[5]]-df1[list2[4]]).round(2)
					my_list1.append(x)

				if x == 'Institutional Holding Change':
					df1[x] = (df1[list2[7]]-df1[list2[6]]).round(2)
					my_list1.append(x)

				if x == 'Mutual Fund Holding Change':
					df1[x] = (df1[list2[9]]-df1[list2[8]]).round(2)
					my_list1.append(x)

				if x == 'Insurance Companies Holding Change':
					df1[x] = (df1[list2[11]]-df1[list2[10]]).round(2)
					my_list1.append(x)

				if x == 'AIF Holding Change':
					df1[x] = (df1[list2[13]]-df1[list2[12]]).round(2)
					my_list1.append(x)

				if x == 'FPI Holding Change':
					df1[x] = (df1[list2[23]]-df1[list2[22]]).round(2)
					my_list1.append(x)

				if x == 'Pension Fund Holding Change':
					df1[x] = (df1[list2[15]]-df1[list2[14]]).round(2)
					my_list1.append(x)

				if x == 'Total Non Institutional Holding Change':
					df1[x] = (df1[list2[17]]-df1[list2[16]]).round(2)
					my_list1.append(x)

				if x == 'Retail Shareholder Change':
					df1[x] = (df1[list2[19]]-df1[list2[18]]).round(2)
					my_list1.append(x)

				if x == 'HNI Holding Change':
					df1[x] = (df1[list2[21]]-df1[list2[20]]).round(2)
					my_list1.append(x)

			df1 = df1[my_list1]

			return df1

		df2 = multi_fun(ft_select)

		if st.sidebar.checkbox("Filters"):
			column = st.sidebar.multiselect("Columns",(ft_select))

			for i in range(0, len(column)):
				name = "filter" + str(i+1)
				filter0 = st.sidebar.text_input(column[i],'>10',key = name)
				#df2 = eval(f"df2[df2['{column[i]}']{filter0}].sort_values(by = '{column[i]}', ascending = False).round(2)")
				df2 = eval(f"df2[df2['{column[i]}']{filter0}].round(2)")

			df2 = df2.rename(columns={'name.of.the.scrip':'Name of Scrip'})
			df2.index = range(len(df2))
			df2.index += 1
			st.table(df2)

		if ft_select == []:
			df2 = df
			df2 = df2.rename(columns={'name.of.the.scrip':'Name of Scrip'})

		def get_file(df):

			csv = df2.to_csv().encode()
			b64 = base64.b64encode(csv).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="Scanner.csv" target="_blank">Download CSV File</a>'
			st.sidebar.markdown(href, unsafe_allow_html=True)

		if st.sidebar.button("Get CSV"):
			get_file(df2)

if __name__ == '__main__':
	main()
