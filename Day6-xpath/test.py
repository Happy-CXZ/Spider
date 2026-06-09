import bcrypt


def generate_bcrypt_hash():
    """输入明文密码，输出 bcrypt 哈希值"""
    password = input("请输入明文密码: ")

    # 生成 bcrypt 哈希（cost=10，可调整）
    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    print(f"\nbcrypt 哈希值: {hashed.decode('utf-8')}")
    print(f"长度: {len(hashed.decode('utf-8'))} 字符")
    print(f"算法: bcrypt (cost=10)")


if __name__ == "__main__":
    generate_bcrypt_hash()