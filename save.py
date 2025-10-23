"""
TextSaver.py
作業者３：文字起こし結果をテキストファイルに保存するモジュール
"""

import os
from datetime import datetime

def save_transcription(text, folder="results"):
    """
    文字起こしされたテキストを上書きせずに保存します。

    Parameters
    ----------
    text : str
        Whisperなどで文字起こしされたテキスト。
    folder : str, optional
        保存先フォルダ名（デフォルトは 'results'）。

    Returns
    -------
    str
        保存されたファイルのパス
    """
    # フォルダが存在しない場合は作成
    os.makedirs(folder, exist_ok=True)

    # 現在時刻で一意なファイル名を作成
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript_{timestamp}.txt"
    filepath = os.path.join(folder, filename)

    # テキストを保存
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"文字起こし結果を {filepath} に保存しました。")
    return filepath


# テスト実行用（単独でも確認できる）
if __name__ == "__main__":
    sample_text = "これは音声認識テストの結果です。"
    save_transcription(sample_text)
