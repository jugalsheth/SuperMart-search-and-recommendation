import streamlit as st
import pandas as pd
import altair as alt
import numpy as np




def main():



	page_bg_img = '''
	<style>
	body {
	background-image: url("https://cdn.shopify.com/s/files/1/2617/9116/products/2046-60-mistyteal_3472a883-658e-4f06-b350-387a8eafa4ae_2000x.png?v=1548285063");
	background-size: cover;
	}
	</style>
	'''

	st.markdown(
    """
	<style>
	.reportview-container .markdown-text-container {
    font-family: monospace;
	}
	.sidebar .sidebar-content {
    background-image: linear-gradient(#f07470, #f1959b, #f6bdc0);
    color: white;
	}
	.Widget>label {
    color: black;
    font-family: monospace;
    font-size:15px;
	}
	</style>
	""",
    unsafe_allow_html=True,
	)

	st.markdown(page_bg_img, unsafe_allow_html=True)

	## Databases


	pass_data=pd.read_csv('Passwords.csv')



	all_pred=pd.read_csv('all_pred.csv')



	reg_lost=pd.read_csv('reg_top_lost.csv')




	popular=pd.read_csv('df_popular.csv')


	group_data=pd.read_csv('output_df.csv')


	pass_data['Customer_ID']=pass_data['Customer_ID'].astype(str)

	data = pd.merge(all_pred,reg_lost.groupby(['Category','Sub-Category','ProductName','ProductID']).count().reset_index()[['Category','Sub-Category','ProductName','ProductID']],how = 'inner', left_on = 'itemID', right_on='ProductID')
	data = pd.merge(data,reg_lost.groupby(['Customer_ID','Customer_Name']).count().reset_index()[['Customer_ID','Customer_Name']],how = 'inner', left_on = 'userID', right_on='Customer_ID')[['ProductID','ProductName','Category','Sub-Category','Customer_ID','Customer_Name','prediction']]

	data = pd.merge(data,group_data,how = 'inner',on='ProductName')[['ProductID','ProductName','Category','Sub-Category','Customer_ID','Customer_Name','prediction','Group']]
	data = data.sort_values(by=['prediction'], ascending = False)

	product = data.groupby(['ProductID','ProductName','Category','Sub-Category','Group']).count().reset_index()[['ProductID','ProductName','Category','Sub-Category','Group']]



	#title=st.title("SuperStore App")
	#st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>{'SuperStore App'}</span>", unsafe_allow_html=True)

	menu = ["WelcomePage","Login","Search", "New Customer"]
	choice = st.sidebar.selectbox("Menu",menu)


	products_cat=['All','Office Supplies','Furniture','Technology']


	if choice == "WelcomePage":
		bgcolor="#010000"
		fontcolor = "#fff"


		html_temp = """
		<div style="background-color:{};padding:10px">
		<h1 style="color:{};text-align:center;">Welcome to SuperStore!</h1>
		</div>
		"""
		st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)

		html_temp1 = """
		<div> <h1 style='text-align: center; color: red;'>Some title</h1> </div>
		"""

		#st.markdown("<p style='text-align: center; color: red;'>Some title</p>", unsafe_allow_html=True)

		st.markdown('<style>h1 { font-size: 72px;background: -webkit-linear-gradient(#0e97d8, #24576f);-webkit-background-clip: text;-webkit-text-fill-color: transparent;}</style>', unsafe_allow_html=True)

		#st.title("Welcome to SuperStore!")
		st.markdown('<style>h2 { font-size: 72px;background: -webkit-linear-gradient(#0e97d8, #24576f);-webkit-background-clip: text;-webkit-text-fill-color: transparent;}</style>', unsafe_allow_html=True)
		st.markdown(" We help you find the products you need!")
		st.image('back.jpg',use_column_width=200)
		st.header("What are looking for today?")
		st.markdown("We understand every customer is unique and we have have recommendations just for YOU!")
		st.markdown("Login to see the recommendations we have for you!")
		st.header("You can search for products you like")
		st.markdown("We also recommend items you may want to see based on your search")

	elif choice == "Login":
		#users = pass_data['Customer_ID'].unique().tolist()
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type = 'password')
		x=pass_data[pass_data['Customer_ID']==username]
		lbtn=st.sidebar.button("Login")

		if lbtn:
			if x.empty:
				st.warning("Invalid User Name/Password")

			elif(username==""):
				st.warning("User Name cannot be empty")
			elif(password==""):
				st.warning("Password cannot be empty")
			elif((x.iloc[0].Customer_ID==username) & (x.iloc[0].Password==password)):
				st.success("Logged in as {}".format(username))
				st.subheader("Recommendations for you:")
				user_top_k = data[data['Customer_ID']==int(username)]
				st.dataframe(user_top_k[['ProductID','ProductName','Category','Sub-Category']].head(10))
			elif((x.iloc[0].Customer_ID!=username) | (x.iloc[0].Password!=password)):
				st.warning("Invalid User Name/Password")



	elif choice == "Search":
		search = st.text_input("Search")
		prod = product[product['ProductName']==search]

		g = prod.groupby(['Group']).count().reset_index()[['Group']]


		if st.button("Search"):

			if prod.empty:
				st.warning("No results found")
			elif(search == prod.iloc[0].ProductName==search):
				st.subheader("Item you searched")
				st.dataframe(prod[['ProductID','ProductName','Category','Sub-Category']].head(1))
				st.subheader("Similar items you may like")
				st.dataframe(product[(product['Group']==g.iloc[0].Group) & (product['ProductName']!=search)][['ProductID','ProductName','Category','Sub-Category']].head(10))

	elif choice == "New Customer":
		st.subheader("Recommendations for you")
		popular = popular.rename(columns={'Category': 'ProductCategory'})
		st.dataframe(pd.merge(popular, product, how = 'inner', on ='ProductID')[['ProductID','ProductName','Category','Sub-Category']].head(10))
		#st.dataframe(pd.merge(popular, product, how = 'inner', on ='ProductID'))
		cat=st.selectbox('Choices:',products_cat)
		sort =st.selectbox('Sort By',['Popularity','Low to High','High to Low'])
		if(cat=='All'):
			st.dataframe(pd.merge(popular, product, how = 'inner', on ='ProductID')[['ProductID','ProductName','Category','Sub-Category','Product_Price','Rating']].head(10))
		else:
			filtered_popular=popular[popular['ProductCategory']==cat]
			if(sort=='Low to High'):
				st.dataframe(pd.merge(filtered_popular, product, how = 'inner', on ='ProductID').sort_values(by='Product_Price',ascending=True)[['ProductID','ProductName','Category','Sub-Category','Product_Price','Rating']].head(10))
			elif(sort=='High to Low'):
				st.dataframe(pd.merge(filtered_popular, product, how = 'inner', on ='ProductID').sort_values(by='Product_Price',ascending=False)[['ProductID','ProductName','Category','Sub-Category','Product_Price','Rating']].head(10))
			else:
				st.dataframe(pd.merge(filtered_popular, product, how = 'inner', on ='ProductID').sort_values(by='Rating',ascending=False)[['ProductID','ProductName','Category','Sub-Category','Product_Price','Rating']].head(10))






if __name__ == '__main__':
	main()
