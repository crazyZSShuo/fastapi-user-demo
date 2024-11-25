import click
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

@click.command()
@click.option('--email', prompt='Enter email', help='用户邮箱')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='用户密码')
@click.option('--superuser', is_flag=True, help='是否是超级管理员')
def create_user(email: str, password: str, superuser: bool = False):
    """创建新用户"""
    db = SessionLocal()
    
    # 检查用户是否已存在
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        click.echo(f"Error: User with email {email} already exists!")
        return
    
    try:
        user = User(
            email=email,
            hashed_password=get_password_hash(password),
            is_superuser=superuser,
            is_active=True
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        click.echo(f"Successfully created {'superuser' if superuser else 'user'}: {email}")
    except Exception as e:
        db.rollback()
        click.echo(f"Error creating user: {str(e)}")
    finally:
        db.close()

if __name__ == '__main__':
    create_user() 