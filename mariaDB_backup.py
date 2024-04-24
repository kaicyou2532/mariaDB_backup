import subprocess
import os
from datetime import datetime, timedelta

# バックアップを保存するディレクトリ
BACKUP_DIR = ""

# バックアップを保存するデータベース
DATABASE = ""

def create_backup():
    # バックアップファイルの命名
    backup_file = os.path.join(BACKUP_DIR, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql")

    # mysqldumpコマンドでバックアップを作成
    subprocess.run(["mysqldump", "-u", "your_username", "-pyour_password", DATABASE, "--result-file", backup_file])

def delete_old_backups():
    # 古いバックアップの削除
    cutoff_date = datetime.now() - timedelta(days=7)
    for filename in os.listdir(BACKUP_DIR):
        if filename.startswith("backup_") and filename.endswith(".sql"):
            file_path = os.path.join(BACKUP_DIR, filename)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time < cutoff_date:
                os.remove(file_path)

if __name__ == "__main__":
    create_backup()
    delete_old_backups()
