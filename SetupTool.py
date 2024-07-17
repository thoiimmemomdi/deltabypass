import subprocess
import sys

def install_package(package_name):
    try:
        # Cài đặt gói qua pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError:
        print(f"Không thể cài đặt gói: {package_name}")

def check_and_install_packages():
    # Danh sách các gói cần thiết
    packages = ['requests']

    for package in packages:
        try:
            # Thử nhập gói để kiểm tra xem nó đã được cài đặt chưa
            __import__(package)
            print(f"Gói '{package}' đã được cài đặt.")
        except ImportError:
            print(f"Gói '{package}' chưa được cài đặt. Đang cài đặt...")
            install_package(package)

if __name__ == "__main__":
    check_and_install_packages()

    # Tiếp tục với phần còn lại của mã
    import requests
    from urllib.parse import urlparse, parse_qs
    import os
    import time

    # Ví dụ về cách sử dụng các thư viện đã cài đặt
    def example_function():
        print("Các thư viện đã được cài đặt thành công!")

    example_function()
