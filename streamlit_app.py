A = {(x*2+31+y/4)/100*50+5}*z
x = st.number_input("S種族値を入力してください", min_value=0)
y = st.number_input("努力値を入力してください", min_value=0)
z = st.number_input("性格補正を入力してください", min_value=0)
st.text(A)
