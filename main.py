import streamlit as st
import pandas as pd

def main():
    st.title('チームごとの順位とスコアの表示')

    team_counter = 1
    team_data = []

    while True:
        team_name = st.text_input("チーム名を入力してください", key=f"team_name_input_{team_counter}")
        if not team_name:
            break  # チーム名が空ならループを終了
        
        score1 = st.number_input("スコア1を入力してください", min_value=0, value=0, step=1, key=f"score1_input_{team_counter}")
        score2 = st.number_input("スコア2を入力してください", min_value=0, value=0, step=1, key=f"score2_input_{team_counter}")
        
        if st.button("チームを追加", key=f"add_button_{team_counter}"):
            team_data.append({'Team': team_name, 'Score1': score1, 'Score2': score2})
        
        team_counter += 1
    if team_data:
        df = pd.DataFrame(team_data)
        
        df['Rank1'] = df['Score1'].rank(ascending=False).astype(int)
        df['Rank2'] = df['Score2'].rank(ascending=False).astype(int)
        df['TotalScore'] = df['Score1'] + df['Score2']
        df['TotalRank'] = df['TotalScore'].rank(ascending=False).astype(int)
        
        st.write('チーム別の順位とスコア:')
        st.table(df[['Team', 'Score1', 'Rank1', 'Score2', 'Rank2', 'TotalScore', 'TotalRank']].reset_index(drop=True))
    else:
        st.write("チームが追加されていません。")

if __name__ == "__main__":
    main()

