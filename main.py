import streamlit as st
import pandas as pd

def main():
    st.title('チームごとの順位とスコアの表示')

    team_data = []

    while True:
        team_name = st.text_input("チーム名を入力してください", key=f"team_name_input_{len(team_data)}")
        if not team_name:
            break  # チーム名が空ならループを終了
        
        score1 = st.number_input("スコア1を入力してください", min_value=0, value=0, step=1, key=f"score1_input_{len(team_data)}")
        score2 = st.number_input("スコア2を入力してください", min_value=0, value=0, step=1, key=f"score2_input_{len(team_data)}")
        
        if st.button("チームを追加"):
            team_data.append({'Team': team_name, 'Score1': score1, 'Score2': score2})
    
    if team_data:
        df = pd.DataFrame(team_data)
    
    if teams:
        df = pd.DataFrame({'Team': teams, 'Score1': scores1, 'Score2': scores2})
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
