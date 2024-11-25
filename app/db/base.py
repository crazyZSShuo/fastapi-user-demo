from app.db.session import Base  # noqa
from app.models.user import User  # noqa

# 将所有模型导入到这里
# 这样在创建数据库表时，所有模型都会被正确注册
