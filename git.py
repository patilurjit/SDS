import pandas as pd
import numpy as np
import streamlit as st
import operator
import base64
import warnings
warnings.filterwarnings("ignore")

def main():

	def load_data():
		data = pd.read_csv("./FinalData.csv")
		return data

	df = load_data()

	col_list1 = ['Price_202103','Price_202012','Price_202009','Price_202006','Price_202003','Price_201912','Price_201909','Price_201906','Price_201903',
			 'Price_201812','Price_201809','Price_201806','Price_201803','Price_201712','Price_201709','Price_201706','Price_201703','Price_201612',
			 'Price_201609','Price_201606','Price_201603','Price_201512','Price_201509','Price_201506','Price_201503','Price_201412','Price_201409',
			 'Price_201406','Price_201403','Price_201312']

	col_list2 = ['no.of.shareholder.below.1.lakh.nominal.capital_202103','no.of.shareholder.below.1.lakh.nominal.capital_202012',
			 'no.of.shareholder.below.1.lakh.nominal.capital_202009','no.of.shareholder.below.1.lakh.nominal.capital_202006',
			 'no.of.shareholder.below.1.lakh.nominal.capital_202003','no.of.shareholder.below.1.lakh.nominal.capital_201912',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201909','no.of.shareholder.below.1.lakh.nominal.capital_201906',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201903','no.of.shareholder.below.1.lakh.nominal.capital_201812',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201809','no.of.shareholder.below.1.lakh.nominal.capital_201806',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201803','no.of.shareholder.below.1.lakh.nominal.capital_201712',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201709','no.of.shareholder.below.1.lakh.nominal.capital_201706',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201703','no.of.shareholder.below.1.lakh.nominal.capital_201612',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201609','no.of.shareholder.below.1.lakh.nominal.capital_201606',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201603','no.of.shareholder.below.1.lakh.nominal.capital_201512',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201509','no.of.shareholder.below.1.lakh.nominal.capital_201506',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201503','no.of.shareholder.below.1.lakh.nominal.capital_201412',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201409','no.of.shareholder.below.1.lakh.nominal.capital_201406',
			 'no.of.shareholder.below.1.lakh.nominal.capital_201403','no.of.shareholder.below.1.lakh.nominal.capital_201312']

	for col in col_list1:
		df[col].astype(int)

	for col in col_list2:
		df[col] = df[col].fillna(value=0)

	col_dict = {'Quarterly Price Change':col_list1,
				'Retail Shareholder Change':col_list2}

	list2 = ["a","b","c","d"]

	st.title("Scanner")

	ft_select = st.sidebar.multiselect("Functionality",("Quarterly Price Change","Retail Shareholder Change"))

	Q1 = st.sidebar.selectbox("Enter Start Quarter",('201312','201403','201406','201409','201412','201503','201506','201509','201512','201603','201606','201609','201612',
						     '201703','201706','201709','201712','201803','201806','201809','201812','201903','201906','201909','201912','202003',
						     '202006','202009','202012','202103'),key = 'quarter1')

	Q2 = st.sidebar.selectbox("Enter End Quarter",('201312','201403','201406','201409','201412','201503','201506','201509','201512','201603','201606','201609','201612',
						     '201703','201706','201709','201712','201803','201806','201809','201812','201903','201906','201909','201912','202003',
						     '202006','202009','202012','202103'),key = 'quarter2')

	def get_Q1(Q1):

		for x in ft_select:

			if x == 'Quarterly Price Change':
				list1 = col_dict.get(x)
				for col in list1:
					if Q1 in col:
						price1 = col
						list2[0] = price1

			if x == 'Retail Shareholder Change':
				list1 = col_dict.get(x)
				for col in list1:
					if Q1 in col:
						rsc1 = col
						list2[2] = rsc1

	def get_Q2(Q2):

		for x in ft_select:
			
			if x == 'Quarterly Price Change':
				list1 = col_dict.get(x)
				for col in list1:
					if Q2 in col:
						price2 = col
						list2[1] = price2

			if x == 'Retail Shareholder Change':
				list1 = col_dict.get(x)
				for col in list1:
					if Q2 in col:
						rsc2 = col
						list2[3] = rsc2

	get_Q1(Q1)
	get_Q2(Q2)
	
	if float(Q1) > float(Q2):
		st.error("Invalid Input : Start Quarter greater than End Quarter")

	else:
		def multi_fun(y = []):

			df1 = df

			my_list1 = ['name.of.the.scrip']

			for x in y:

				if x == 'Quarterly Price Change':
					df1[x] = (((df1[list2[1]]-df1[list2[0]])/df1[list2[0]])*100).round(2)
					my_list1.append(x)

				if x == 'Retail Shareholder Change':
					df1[x] = (((df1[list2[3]]-df1[list2[2]])/df1[list2[2]])*100).round(2)
					my_list1.append(x)

			df1 = df1[my_list1]

			return df1

		df2 = multi_fun(ft_select)

		if st.sidebar.checkbox("Filters"):
			column = st.sidebar.multiselect("Columns",(ft_select))

			for i in range(0, len(column)):
				name = "filter" + str(i+1)
				filter0 = st.sidebar.text_input(column[i],'>10',key = name)
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
