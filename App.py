import pandas as pd 
#import plotly.express as px
import streamlit as st 
import warnings
#import pymysql
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
#from matplotlib import pyplot as plt
warnings.filterwarnings("ignore")
st. set_page_config(layout="wide")

#Data_Aggregated_Transaction_df= pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Aggregated_Transaction_Table.csv")
#Data_Aggregated_User_Summary_df= pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Aggregated_User_Summary_Table.csv")
#Data_Aggregated_User_df= pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Aggregated_User_Table.csv")
#Scatter_Geo_Dataset =  pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Map_Districts_Longitude_Latitude1.csv")
#Coropleth_Dataset =  pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Map_IndiaStates_TU.csv")
#Data_Map_Transaction_df = pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Map_Transaction_Table.csv")
#Data_Map_User_Table= pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Data_Map_User_Table.csv")
#Indian_States= pd.read_csv(r"C:\Users\Sylvester\Desktop\Streamlit\Phonepe\pulse\CSV\Longitude_Latitude_State_Table.csv")

column_T1,column_T2 = st.columns([2,8])
with column_T2:
    st.title(':violet[PhonePe Pulse Data_Visualization & Exploration ]')


c1, c2 = st.columns(2)
with c1:
    Year = st.selectbox(
        "Select the year",
        ('2018', '2019', '2020', '2021', '2022'))
with c2:
    Quarter = st.selectbox(
        'Select the Quarter',
        ('1', '2', '3', '4')
    )

year = int(Year)
quarter = int(Quarter)

#Transaction_Scatter_Districts = Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year) & (Data_Map_Transaction_df['Quarter'] == quarter) ].copy()
#Transaction_Coropleth_States = Transaction_Scatter_Districts[Transaction_Scatter_Districts["State"] == "india"]
#Transaction_Scatter_Districts.drop(Transaction_Scatter_Districts.index[(Transaction_Scatter_Districts["State"] == "india")],axis = 0, inplace = True)

#Scattergeo Data
#Transaction_Scatter_Districts = Transaction_Scatter_Districts.sort_values(by = ['Place_Name'], ascending = False)
#Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by = ['District'], ascending = False)

#Total_Amount = []
#for i in Transaction_Scatter_Districts['Total_Amount']:
#    Total_Amount.append(i)
#Scatter_Geo_Dataset['Total_Amount'] = Total_Amount
#Total_Transaction = []
#for i in Transaction_Scatter_Districts['Total_Transactions_count']:
 #   Total_Transaction.append(i)
#Scatter_Geo_Dataset['Total_Transactions'] = Total_Transaction
#Scatter_Geo_Dataset['Year_Quarter'] = str(year) + '-Q' +str(Quarter)


#Coropleth Data
#Coropleth_Dataset = Coropleth_Dataset.sort_values(by = ['state'], ascending = False)
#Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by = ['Place_Name'], ascending = False)
#Total_Amount = []
#for i in Transaction_Coropleth_States['Total_Amount']:
 #   Total_Amount.append(i)
#Coropleth_Dataset['Total_Amount'] = Total_Amount
#Total_Transaction = []
#for i in Transaction_Coropleth_States['Total_Transactions_count']:
 #   Total_Transaction.append(i)
#Coropleth_Dataset['Total_Transactions'] = Total_Transaction


#Fig1 India Map
#Indian_States = Indian_States.sort_values(by = ['state'], ascending =False)
#Indian_States['Registered_Users'] = Coropleth_Dataset['Registered_Users']
#Indian_States['Total_Amount'] = Coropleth_Dataset['Total_Amount']
#Indian_States['Total_Transactions'] = Coropleth_Dataset['Total_Transactions']
#Indian_States['Year_Quarter'] = str(year) + '-Q' + str(quarter)

#fig = px.scatter_geo(Indian_States,
 #                    lon = Indian_States['Longitude'],
  #                   lat = Indian_States['Latitude'],
   #                  text = Indian_States['code'], #displau district name on map
    #                 hover_name = "state",
     #                hover_data = ['Total_Amount','Total_Transactions','Year_Quarter']
      #               )

#fig.update_traces(marker = dict(color = "white", size = 0.3))
#fig.update_geos(fitbounds = "locations", visible = False)


#Scatter Plotting Districts
#Scatter_Geo_Dataset['col'] = Scatter_Geo_Dataset['Total_Transactions']
#fig1 = px.scatter_geo(Scatter_Geo_Dataset,
 #                     lon = Scatter_Geo_Dataset['Longitude'],
  #                    lat = Scatter_Geo_Dataset['Latitude'],
   #                   color = Scatter_Geo_Dataset['col'],
    #                  size = Scatter_Geo_Dataset['Total_Transactions'],
     #                 hover_name = "District",
      #                hover_data = ["State", "Total_Amount", "Total_Transactions", "Year_Quarter"],
       #               title = 'District',
        #              size_max = 22
         #             )
#fig1.update_traces(marker = dict(color = "blue", line_width = 1))

#Coropleth Mapping India
#fig_ch = px.choropleth(Coropleth_Dataset,
 #                      geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
  #                     featureidkey = 'properties.ST_NM',
   #                    locations = 'state',
    #                   color = "Total_Transactions")
#fig_ch.update_geos(fitbounds = "locations", visible = False)


#Combine States, Districts and Choropleth
#fig_ch.add_trace(fig.data[0])
#fig_ch.add_trace(fig1.data[0])
st.write("### **:blue[PhonePe India Map]**")
colT1,colT2 = st.columns([6,6])
with colT1:
   # st.plotly_chart(fig_ch, use_container_width = True)
#with colT2:
    #st.info(
        """Map Details:\n

            * Darkness of state -> Total Transactions \n
            * Size of the circles -> Total Transaction District-wise \n
            * Bigger the circle Higher the Transactions \n 
            * Hover_Data shows Total Transactions and Total Amount \n
            """
   # )



##Figure2 Hidden Bargraph
#Coropleth_Dataset = Coropleth_Dataset.sort_values(by = ['Total_Transactions'])
#fig = px.bar(Coropleth_Dataset, x = 'state',
 #            y = 'Total_Transactions',
  #           title = str(year) + "Quarter-" + str(quarter))
with st.expander("See Bargraph for the same data"):
    #st.plotly_chart(fig, use_container_width = True)
    #st.info('**:indigo[The above graph shows the increasing order of Phonepe Transactions regarding the states of India.**]')

##Transaction Analysis
#st.write('# :violet[Transaction Analysis : currency_exchange:]')
#tab1, tab2, tab3, tab4 = st.tabs(["State Analysis", "District Analysis", "Year Analysis", "Overall Analysis"])

#Transaction Figure1 State Analysis
with tab1:
#    Data_Aggregated_Transaction = Data_Aggregated_Transaction_df.copy()
 #   Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(Data_Aggregated_Transaction["State"] == "India")], axis = 0, inplace = True)
  #  State_PaymentMode = Data_Aggregated_Transaction.copy()
    col1, col2 = st.columns(2)
    with col1:
        mode = st.selectbox('Select the Mode',
                            ('Recharge & bill payments', 'Peer-to-peer payments',
                             'Financial Services', 'Others'), key = 'a')
    with col2:
        state = st.selectbox('Select the State',
                             ('andaman-&-nicobar-islands','andhra-pradesh', 'arunachal-pradesh',
                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa',
                              'gujarat', 'haryana', 'himachal-pradesh', 
                              'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala',
                              'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                              'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                              'uttar-pradesh', 'uttarakhand', 'west-bengal'), key = 'b')
        
    State = state
    Year_List = [2018, 2019, 2020, 2021, 2022]
    Mode = mode
   # State_PaymentMode = State_PaymentMode.loc[(State_PaymentMode['State'] == State) & (State_PaymentMode['Year'].isin(Year_List)) &
    #                                          (State_PaymentMode['Payment_Mode'] == Mode)]
    #State_PaymentMode = State_PaymentMode.sort_values(by = ['Year'])
    #State_PaymentMode["Quarter"] = "Q" + State_PaymentMode['Quarter'].astype(str)
    #State_PaymentMode["Year_Quarter"] = State_PaymentMode['Year'].astype(str) +"-" + State_PaymentMode["Quarter"].astype(str)

    #fig = px.bar(State_PaymentMode, x = 'Year_Quarter', y = 'Total_Transactions_count', color = "Total_Transactions_count",
     #            color_continuous_scale = "Viridis")
    
    colT1, colT2 = st.columns([7,7])
    with colT1:
        st.write('###' + State.upper())
       # st.plotly_chart(fig, use_container_width = True)
    #with colT2:
       # st.info("""
        #BarGraph Details:\n
         #          * This data belongs to state selected by us\n
          #         * X Axis -> All years with all quarters\n
           #        * Y Axis -> Total Transactions""")
        



##Transaction Figure2 District Analysis
with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        Year = st.selectbox(
            'Select the Year',
            ('2018', '2019', '2020', '2021', '2022'),key = 'y1'

        )
    with col2:
        state = st.selectbox('Select the State',
                             ('andaman-&-nicobar-islands','andhra-pradesh', 'arunachal-pradesh',
                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa',
                              'gujarat', 'haryana', 'himachal-pradesh', 
                              'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala',
                              'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                              'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                              'uttar-pradesh', 'uttarakhand', 'west-bengal'), key = 'dk')
    with col3:
        Quarter = st.selectbox(
            'Select the Quarter',
            ('1', '2', '3', '4'), key = 'qwe'
        )

    #districts = Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['State'] == state) & (Data_Map_Transaction_df['Year'] == int(Year))
     #                                              & (Data_Map_Transaction_df['Quarter'] == int(Quarter))]
    #l = len(districts)
    #fig = px.bar(districts, x = 'Place_Name', y = 'Total_Transactions_count', color = "Total_Transactions_count",
      #           color_continuous_scale="Viridis")
    colT1, colT2 = st.columns([7,7])
    with colT1:
        st.write('###' + state.upper() + ' With ' + str(l) + 'Districts')
       # st.plotly_chart(fig,use_container_width=True)
    #with colT2:
     #   st.info("""
      #           BarGraph Details:\n
       #                      * Data belongs to state gets selected by us\n
        #                     * X Axix -> Districts of selected state
         #                    * Y Axis -> Total Transactions
          #                   """
           #     )


##Transaction Figure3 Analysis
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        M = st.selectbox('Select the Mode',
                         ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial services', 'Others'), key ='D')
        
    with col2:
        Y = st.selectbox('Select the Year',
                         ('2018', '2019', '2020', '2021', '2022'), key = 'F')
    
    #Year_PaymentMode = Data_Aggregated_Transaction.copy()
    Year = int(Y)
    Mode = M
    Y#ear_PaymentMode = Year_PaymentMode.loc[(Year_PaymentMode['Year'] == Year) &
                                            #(Year_PaymentMode['Payment_Mode'] == Mode)]
    #States_List = Year_PaymentMode['State'].unique()
    #State_groupby_YP = Year_PaymentMode.groupby('State')
    #Year_PaymentMode_Table = State_groupby_YP.sum()
    #Year_PaymentMode_Table['states'] = States_List
    #del Year_PaymentMode_Table['Quarter']
    #del Year_PaymentMode_Table['Year']
    #Year_PaymentMode_Table = Year_PaymentMode_Table.sort_values(by = ['Total_Transactions_count'])
    #fig2 = px.bar(Year_PaymentMode_Table, x = 'states', y = 'Total_Transactions_count', color = "Total_Transactions_count",
     #             color_continuous_scale="Viridis")
    
    colT1, colT2 = st.columns([7,7])
    with colT1:
        st.write('###' + str(Year) + ' Data Analysis ')
        #st.plotly_chart(fig2, use_container_width=True)
    #with colT2:
     #   st.info("""
      #             Bargraph Details:\n
       #                         * Data belongs to selected year by us
        #                        * X Axis -> States in increasing order of Total Transactions
         #                       * Y Axis -> Total Transactions
          #                      """
           #     )
        
##Transaction Figure4 Overall Analysis
with tab4:
    #years = Data_Aggregated_Transaction.groupby('Year')
    #years_List = Data_Aggregated_Transaction['Year'].unique()
    #years_Table = years.sum()
    #del years_Table['Quarter']
    #years_Table['year'] = years_List
    #total_trans = years_Table['Total_Transactions_count'].sum()
    #fig1 = px.pie(years_Table, values = 'Total_Transactions_count', names = 'year',
     #             color_discrete_sequence = px.colors.sequential.Viridis, title = 'Total Transactions 2018 to 2022')
    #col1, col2 = st.columns([0.65, 0.35])
    with col1:
        st.write('### :blue[Drastical Increase in Transactions]')
        #st.plotly_chart(fig1)
    #with col2:
        st.write('### :blue[Year Wise Transaction Analysis in India]')
        st.markdown(years_Table.style.hide(axis = 'index').to_html(), unsafe_allow_html=True)
     #   st.info("""We can see that the online transactions has drastically every year""")

# $$$$$$$$$$$$$$$$$$$$$$$$$ USER ANALYSIS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
st.write('# :violet[User Data Analysis]')
tab1, tab2, tab3, tab4 = st.tabs(["State Analysis", "District Analysis", "Year Analysis", "Overall Analysis"])

#User State Analysis
with tab1:
    st.write('### :blue[State & Userbase]')
    state = st.selectbox('Select the State',
                             ('andaman-&-nicobar-islands','andhra-pradesh', 'arunachal-pradesh',
                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa',
                              'gujarat', 'haryana', 'himachal-pradesh', 
                              'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala',
                              'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                              'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                              'uttar-pradesh', 'uttarakhand', 'west-bengal'), key = 'W')
    
    #app_opening = Data_Aggregated_User_Summary_df.groupby(['State', 'Year'])
    #a_state = app_opening.sum()
    #la = Data_Aggregated_User_Summary_df['State'] + "-" + Data_Aggregated_User_Summary_df["Year"].astype(str)
    #a_state["state_year"] = la.unique()
    #sta = a_state["state_year"].str[:-5]
    #a_state["state"] = sta
    #sout = a_state.loc[(a_state['state'] == state)]
    #ta = sout['AppOpenings'].sum()
    #tr = sout['Registered_Users'].sum()
    #sout['AppOpenings'] = sout['AppOpenings'].mul(100/tr).copy()
    #fig = go.Figure(data = [
     #   go.Bar(name = 'AppOpenings %', y =sout['AppOpenings'], x = sout['state_year'], marker = {'color' : 'red'}),
      #  go.Bar(name = 'Registered_Users %', y = sout['Registered_Users'], x = sout['state_year'], marker = {'color' : 'lightgreen'})

    #])
    #fig.update_layout(barmode = 'group')
    colU1, colU2 = st.columns([7,7])
    with colU1:
        st.write("###", state.upper())
       # st.plotly_chart(fig, use_container_width=True, height =200)

    #with colU2:
     #   st.info("""
                  Bargraph Details:\n
                                * Select a state\n
                                * X Axis -> Registered_Users and App Openings\n
                                * Y Axis -> Percentage of Registered_users and App Openings
                                """
           #     )
    
## User District Analysis

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        Year = st.selectbox(
            'Select the Year',
            ('2018', '2019', '2020', '2021', '2022'),key = 'y12'

        )
    with col2:
        state = st.selectbox('Select the State',
                             ('andaman-&-nicobar-islands','andhra-pradesh', 'arunachal-pradesh',
                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa',
                              'gujarat', 'haryana', 'himachal-pradesh', 
                              'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala',
                              'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                              'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                              'uttar-pradesh', 'uttarakhand', 'west-bengal'), key = 'dk2')
    with col3:
        Quarter = st.selectbox(
            'Select the Quarter',
            ('1', '2', '3', '4'), key = 'qwe2'
        )
    
    #districts = Data_Map_User_Table.loc[(Data_Map_User_Table['State'] == state) & (Data_Map_User_Table['Year'] == int(Year))
                                       # &(Data_Map_User_Table['Quarter'] == int(Quarter))]
    #l = len(districts)
    #fig = px.bar(districts, x = 'Place_Name', y = 'App_Openings', color = "App_Openings",
     #            color_continuous_scale="reds")
    colU1, colU2 = st.columns([7,7])
    with colU1:
        if l:
            st.write('###' +state.upper()+ 'With' + str(l) + 'Districts')
          #  st.plotly_chart(fig, use_container_width=True)

        else:
            st.write('### Districts data is not available for' + state.upper())
        
   # with colU2:
    #    if l:
     #       st.info("""
                      Bargraph Details:\n
                                 * Data belongs to state selected by us\n
                                 * X Axix -> Districts from selected state\n
                              * Y Axis -> App Openings"""
            #)

        
##User Year Analysis
with tab3:
    st.write('### :blue[Brand Share]')
    col1, col2 = st.columns(2)
    with col1:
        state = st.selectbox('Select the State',
                             ('andaman-&-nicobar-islands','andhra-pradesh', 'arunachal-pradesh',
                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa',
                              'gujarat', 'haryana', 'himachal-pradesh', 
                              'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala',
                              'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                              'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                              'uttar-pradesh', 'uttarakhand', 'west-bengal'), key = 'Z')
    with col2:
        Y = st.selectbox(
            'Select the Year',
            ('2018', '2019', '2020', '2021', '2022'),key = 'X'

        )
    y = int(Y)
    s = state
    #brand = Data_Aggregated_User_df[Data_Aggregated_User_df['Year'] == y]
    #brand = Data_Aggregated_User_df.loc[(Data_Aggregated_User_df['Year'] == y) & (Data_Aggregated_User_df['State'] == s)]
    #myb = brand['Brand_Name'].unique()
    #x = sorted(myb).copy()
    #b = brand.groupby('Brand_Name').sum()
    #b['brand'] = x
    #br = b['Registered_Users_Count'].sum()
    #labels = b['brand']
    #values = b['Registered_Users_Count']
    #fig3 = go.Figure(data = [go.Pie(labels = labels, values = values, hole = .4, textinfo = 'label+percent', texttemplate = '%{label}<br>%{percent:1%f}', insidetextorientation= 'horizontal', textfont = dict(color = '#000000'),marker_colors = px.colors.qualitative.Prism)])

    colU1, colU2 = st.columns([7,7])
    with colU1:
        st.write("###", state.upper() + 'in' + Y)
       # st.plotly_chart(fig3, use_container_width=True)
    #with colU2:
     #   st.info("""
                   Chart Details : \n
                               * Select the data by means of State and Year
                               * Percentage of Registered_Users represented with Chart through Device Brand
                               """
      #          )
    b = b.sort_values(by = ['Registered_Users_Count'])
    fig4 = px.bar(b, x = 'brand', y = 'Registered_Users_Count', color = "Registered_Users_Count",
                  title = 'In ' + state + 'in ' + str(y),
                  color_continuous_scale= "peach")
    with st.expander("See Bargraph for same data"):
        st.plotly_chart(fig4, use_container_width=True)
    

## User Overall Analysis
with tab4:
    #years = Data_Aggregated_User_Summary_df.groupby('Year')
    #years_List = Data_Aggregated_User_Summary_df['Year'].unique()
    #years_Table = years.sum()
    #del years_Table['Quarter']
    #years_Table['year'] = years_List
    #total_trans = years_Table['Registered_Users'].sum()
    #fig1 = px.pie(years_Table, values = 'Registered_Users', names = 'year', color_discrete_sequence = px.colors.sequential.Rainbow, title = 'Total Registered_Users (2018 to 2022)')
    col1, col2 = st.columns([0.7,0.3])
    with col1:
        labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India", "Rest of World"]
        fig = make_subplots(rows = 1, cols =2, specs = [[{'type' : 'domain'}, {'type' : 'domain'}]])
        fig.add_trace(go.Pie(labels = years_Table['year'], values = years_Table['Registered_Users'], name = "Registered_Users"), 1, 1)
        fig.add_trace(go.Pie(labels = years_Table['year'], values = years_Table['AppOpenings'], name = "App Openings"), 1, 2)

        fig.update_traces(hole = .6, hoverinfo = "label+percent+name")

        fig.update_layout(
            title_text = "Users Data 2018 to 2022",
            annotations = [dict(text = 'Users', x = 0.18, y = 0.5, font_size = 20, showarrow = False),
                           dict(text = 'App', x = 0.82, y = 0.5, font_size = 20, showarrow = False)]
        )
        st.plotly_chart(fig)
    
    with col2:
        st.markdown(years_Table.style.hide(axis = 'index').to_html(), unsafe_allow_html=True)
        st.info("""
                   We Can see that Registered_Users and App Openings tend to increase every year""")
        
st.write('## :pink[Top 3 States Data]')
c1,c2 = st.columns(2)
with c1:
    Year = st.selectbox(
            'Select the Year',
            ('2018', '2019', '2020', '2021', '2022'),key = 'y1h2k'

        )
with c2:
    Quarter = st.selectbox(
            'Select the Quarter',
            ('1', '2', '3', '4'), key = 'qgwe2'
        )
    
#Data_Map_User_df = Data_Aggregated_User_Summary_df.copy()
#top_states = Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] == int(Quarter))]
#top_states_r = top_states.sort_values(by = ['Registered_Users'], ascending = False)
#top_states_a = top_states.sort_values(by = ['AppOpenings'], ascending = False)

#top_states_T = Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(Year)) & (Data_Aggregated_Transaction_df['Quarter'] == int(Quarter))]
#topst = top_states_T.groupby('State')
#x = topst.sum().sort_values(by = ['Total_Transactions_count'], ascending=False)
#y = topst.sum().sort_values(by = ['Total_Amount'], ascending=False)
col1, col2, col3, col4 = st.columns([2.5, 2.5, 2.5, 2.5])

with col1:
    rt = top_states_r[1:4]
    st.markdown("### :pink[Registered_Users]")
    st.markdown(rt[[ 'State', 'Registered_Users']].style.hide(axis = "index").to_html(), unsafe_allow_html=True)

with col2:
    at = top_states_r[1:4]
    st.markdown("### :pink[PhonePe App Openings]")
    st.markdown(at[[ 'State', 'AppOpenings']].style.hide(axis = "index").to_html(), unsafe_allow_html=True)

with col3:
    st.markdown("### :pink[Total Transactions]")
    st.write(x[['Total_Transactions_count']][1:4])

with col4:
    st.markdown("### :pink[Total Amount]")
    st.write(y['Total_Amount'][1:4])










    
