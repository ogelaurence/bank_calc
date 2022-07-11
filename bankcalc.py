import streamlit as st
import datetime
st.sidebar.header(" Welcome to our interest calculator")
from PIL import Image
image= Image.open('bank.jpg')
st.sidebar.image(image, caption = " ")
dep_opt= ['Savings Deposit', 'Call Deposit','Term Deposit']
loan_opt = ['Personal Loan', 'Mortgage Loan']
opt_list= ['Deposit','Loan']

click_opt = st.sidebar.radio(" Choose an option ", opt_list)


if click_opt == 'Deposit' :
    click_dep = st.sidebar.radio(' What type of Deposit account? : ',dep_opt)
    no = (dep_opt).index(click_dep) # this provides the index no to use for the deposit ption for calculations later.
    if  click_dep :
        st.sidebar.write (f'''Review the checklist below and select''')
        st.sidebar.error( f''' Note all 3 items listed below must be available to proceed.''')
        
        dep_amt_sel = st.sidebar.checkbox(" Do you have the intended Deposit amount? ")
        dep_rate_sel = st.sidebar.checkbox(" Do you have the current bank Deposit Interest rate? ")
        dep_ten_sel = st.sidebar.checkbox(" Do you have your intended Deposit Tenor? ")
        st.sidebar.button(" Proceed ")
        dep_pro = dep_amt_sel and dep_rate_sel and dep_ten_sel
        
        
        if dep_pro:
            st.write(f''' We would calculate the Interest you would get on your deposit with the Bank. ''')
                
            damt = st.number_input( " Input the amount : ")
            drate = st.number_input(  " Current Rate ")
            col1,col2 = st.columns(2)
            with col1:
                ddur = ['Days','Months']
                dten = int(st.number_input( " Tenor "))
            with col2: 
                d_ten_dur = st.radio(" What tenor unit? ",ddur )
                
                if d_ten_dur == 'Days':
                    dep_int = round((damt * drate * dten) / (100 *365),2)
                    dep_finalbal = round(damt + dep_int,2)
                    
                else :
                    dep_int = round((damt * drate * dten * 30) / (100 *365),2)
                    dep_finalbal = round(damt + dep_int,2)
                    
                wht = round((0.075 * dep_int),2)
                dep_int_new = round(dep_int - wht,2)
                dep_finalbal_new = damt + dep_int_new

            if st.button(' Generate Interest '):
                st.write(f''' Your would earn N{dep_int} on your deposit after {dten} {d_ten_dur} ''')
                st.error(" Kindly note that WHT (WithHolding Tax) is taken on the interest generated. ")
                st.write(f''' Your Interest after withHolding tax of 7.5%  is N{dep_int_new} \n
                             Your final account balance would be N{dep_finalbal_new}   ''')
                
        else:
            st.error(" All information in the checklist must be available to proceed. ")
            st.subheader(f''' Kindly review the checklist and select accordingly. ''')
    
    
elif click_opt == 'Loan':
    click_loan = st.sidebar.radio('What type of Loan? :',loan_opt)
    no = (loan_opt).index(click_loan) # this provides the index no to use for the deposit ption for calculations later.
    if click_loan :
        #para = [' Loan Amount', 'Bank Rate','Tenor']
        st.sidebar.write (f'''Review the checklist below: ''')                
        st.sidebar.error(f''' Note all 3 items listed below must be available to proceed.''')
        loan_amt_sel = st.sidebar.checkbox(" Do you have your intended Loan amount? ")
        loan_rate_sel = st.sidebar.checkbox(" Do you have the current bank Loan Interest rate? ")
        loan_ten_sel = st.sidebar.checkbox(" Do you have your intended Loan Tenor? ")
        st.sidebar.success(f" Optional : Only needed if you wish to know upfront charges when loan is disbursed.")
        loan_mgt_fee = st.sidebar.checkbox(" Do you have the bank's Management fee rate? ")
        loan_pro_fee = st.sidebar.checkbox(" Do you have the bank's Processing fee rate? ")
        loan_ins_fee = st.sidebar.checkbox(" Do you have the bank's Credit Insurance rate? ")
        st.sidebar.button(" Proceed ")
        loan_pro = loan_amt_sel and loan_rate_sel and loan_ten_sel 
        if loan_pro and click_loan == 'Personal Loan':
            st.markdown(f''' We would calculate the Interest you would pay for your loan with the Bank. ''')
            
            salary = float(st.number_input (" What's your current Monthly salary? : "))
            loan_amt = float(st.number_input(" Input the desired loan amount : "))
            loan_rate = float(st.number_input( "What is the bank's current Personal loan Rate? :"))  
            loan_ten = int(st.slider(" What's your desired Loan tenor in Months? ", 6 , 60))
            st.success(" Optional : Inputs below are only needed if you wish to know your upfront charges for the loan.")
            col1,col2,col3 = st.columns(3)
            with col1:
                loan_mgt = float(st.number_input( " Input the Bank's Loan Management Fee Rate : "))
            with col2:
                loan_pro = float(st.number_input( " Input the bank's Loan Processing Fee rate: "))
            with col3:
                loan_ins = float(st.number_input(" Input the bank's credit insurance rate :"))
            
            loan_int = round((loan_amt * 30 * loan_rate)/(36500),2)
            mth_princ = round((loan_amt/loan_ten),2)
            mth_repay = round((mth_princ + loan_int),2)

            max_mth_repay = round((salary * 0.33),2)
            
            if st.button(' Generate Interest '):
                if mth_repay < max_mth_repay :
                    st.write(f" Your interest would be N{loan_int} per month    ")
                    st.success( f" Your payment every month would be estimated at N{mth_repay} over the {loan_ten} months")
                    if loan_mgt and loan_pro and loan_ins :
                        mgt_fee = round((loan_amt * loan_mgt)/100,2)
                        pro_fee = round((loan_amt * loan_pro)/100,2)
                        ins_fee = round((loan_amt * loan_ins)/100,2)
                        st.write(f''' Upfront Management Fee charge would be N{mgt_fee} \
                                    Processing Fee charge would be N{pro_fee} \
                                    Insurance Fee charge would be N{ins_fee}''')
                        Tot_fee = mgt_fee+pro_fee+ins_fee
                        st.success(f" Total one-off Upfront Charges is estimated at : N{Tot_fee} " )
                        
                else :
                    st.error(f" Your maximum monthly total repayment cannot not exceed N{max_mth_repay}.")
                    st.write(f" For the sum of N{loan_amt}, the monthly repayment would be N{mth_repay}." )
                    st.write(" You cannot access up to your desired amount, Kindly reduce the loan amount or increase your loan tenor(if aplicable) and try again. ") 
            
        elif loan_pro and click_loan == 'Mortgage Loan':
            st.markdown(f''' We would calculate the Interest you would pay for your Mortgage loan with the Bank. ''')
            mort_salary = float(st.number_input (" What's your current Monthly salary? : "))
            age = int(st.slider(" How old are you? ", 18,60))
            mort_amt = float(st.number_input(" Input the desired Mortgage amount : "))
            mort_rate = float(st.number_input( "What is the bank's current Mortgage loan Rate? :"))  
            mort_ten = int(st.slider(" What's your desired Mortgage tenor in Years? ",1,30))
            st.success(" Optional : Inputs below are only needed if you wish to know your upfront charges for the loan.")
            col1,col2,col3 = st.columns(3)
            with col1:
                mort_mgt = float(st.number_input( " Input the Bank's Mortgage Loan Management Fee Rate : "))
            with col2:
                mort_pro = float(st.number_input( " Input the bank's Mortgage Loan Processing Fee rate: "))
            with col3:
                mort_ins = float(st.number_input(" Input the bank's Mortgage insurance rate :"))
            
            mort_dur = int(60 - age) # this is the space of time possible to pay the loan.
            if mort_dur > mort_ten:
                mort_int = round((mort_amt * 30 * mort_rate)/(36500),2)
                mort_mth_princ = round(mort_amt/(mort_ten*12),2)
                mort_mth_repay = round((mort_mth_princ + mort_int),2)

                max_mort_mth_repay = round((mort_salary * 0.33),2)
                
                if st.button(' Generate Interest '):
                    if mort_mth_repay < max_mort_mth_repay :
                        st.write(f" Your interest would be N{mort_int} per month ")
                        st.success( f" Your payment every month would be estimated at N{mort_mth_repay} over the {mort_ten} Years")
                        if mort_mgt and mort_pro and mort_ins :
                            mort_mgt_fee = round((mort_amt * mort_mgt)/100,2)
                            mort_pro_fee = round((mort_amt * mort_pro)/100,2)
                            mort_ins_fee = round((mort_amt * mort_ins)/100,2)
                            st.write(f''' Upfront Management Fee charge would be N{mort_mgt_fee} \
                                        Processing Fee charge would be N{mort_pro_fee} \
                                        Insurance Fee charge would be N{mort_ins_fee}''')
                            mort_tot_fee = mort_mgt_fee+mort_pro_fee+mort_ins_fee
                            st.success(f" Total one-off Upfront Charges is estimated at : N{mort_tot_fee} " )
                        
                    else :
                        st.error(f" Your maximum monthly total repayment cannot not exceed N{max_mort_mth_repay}.")
                        st.write(f" For the sum of N{mort_amt}, the monthly repayment would be N{mort_mth_repay}." )
                        st.write(" You cannot access up to your desired amount, Kindly reduce the loan amount or increase your loan tenor(if aplicable) and try again. ") 
            
            else:
                st.error(f" Your loan repayment must end before the official retirement age. Kindly readjust the loan duration.")
             
        else:
                st.error(" All information in the checklist must be available to proceed. ")
                st.subheader(f''' Kindly review the checklist and select accordingly. ''')
else: 
    st.stop("")
    


