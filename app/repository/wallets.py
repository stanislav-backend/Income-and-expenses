from app.database import SessionLocal
from app.models import Wallet
from decimal import Decimal
from sqlalchemy.orm import Session
from app.models import User


def is_wallet_exist(db: Session, user_id: int, wallet_name: str) -> bool:
    return db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first() is not None


def add_income(db: Session, user_id: int, wallet_name: str, amount: Decimal) -> Wallet:

    wallet = db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()
    if wallet is None:
        raise ValueError(f"Wallet '{wallet_name}' does not exist.")
    wallet.balance += amount
    return wallet

def get_wallet_balance_by_name(db: Session, user_id: int, wallet_name: str) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()
    if wallet is None:
        raise ValueError(f"Wallet '{wallet_name}' does not exist.")
    return wallet


def add_expense(db: Session, user_id: int, wallet_name: str, amount: Decimal) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()
    if wallet is None:
        raise ValueError(f"Wallet '{wallet_name}' does not exist.")
    wallet.balance -= amount
    return wallet


def get_all_wallets(db: Session, user_id: int) -> list[Wallet]:
    wallets = db.query(Wallet).filter(Wallet.user_id == user_id).all()
    return wallets


def create_wallet(db: Session, user_id: int, wallet_name: str, amount: float) -> Wallet:
    wallet = Wallet(name=wallet_name, balance=amount, user_id=user_id)
    db.add(wallet)
    db.flush() 
    return wallet