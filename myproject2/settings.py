import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY は環境変数から取得。設定されていない場合はその場で生成 (本番環境では非推奨)
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())

# DEBUG も環境変数から取得。設定されていない場合は False
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS も環境変数から取得 (カンマ区切りで複数指定可能)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# ... (他の設定はそのまま) ...

# 静的ファイルの設定
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # 本番環境用のディレクトリ
# STATICFILES_DIRS = [BASE_DIR / "static"] # プロジェクト共通の静的ファイルがある場合