import streamlit as st
import pandas as pd

def main():
    st.title('チームごとの順位とスコアの表示')

    teams = []
    scores1 = []
    scores2 = []

    team_name = st.text_input("チーム名を入力してください")
    while team_name:
        score1 = st.number_input("みやわきッキングスナイパー", min_value=0, value=0, step=1)
        score2 = st.number_input("ボウリングストライカー", min_value=0, value=0, step=1)
        
        if st.button("チームを追加"):
            teams.append(team_name)
            scores1.append(score1)
            scores2.append(score2)
        
        team_name = st.text_input("チーム名を入力してください")
    
    if teams:
        df = pd.DataFrame({'Team': teams, 'Score1': scores1, 'Score2': scores2})
        
        # 各スコアごとに順位を付与
        df['Rank1'] = df['Score1'].rank(ascending=False).astype(int)
        df['Rank2'] = df['Score2'].rank(ascending=False).astype(int)
        
        # スコア1とスコア2の合計を計算し、合計に基づいて順位を付与
        df['TotalScore'] = df['Score1'] + df['Score2']
        df['TotalRank'] = df['TotalScore'].rank(ascending=False).astype(int)
        
        st.write('チーム別の順位とスコア:')
        st.table(df[['Team', 'Score1', 'Rank1', 'Score2', 'Rank2', 'TotalScore', 'TotalRank']].reset_index(drop=True))
    else:
        st.write("チームが追加されていません。")

if __name__ == "__main__":
    main()
