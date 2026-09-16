import asyncio
from app.locket_client import LocketActivator

async def main_async():
    print("=" * 65)
    print("      TOOL KÍCH HOẠT LOCKET GOLD (BÓC TÁCH TỪ GITHUB)")
    print("=" * 65)
    
    # Nhập thông tin trực tiếp qua console input()
    target_uid = input("  > Nhập Locket Username hoặc UID cần kích hoạt: ").strip()
    if not target_uid:
        print("[❌ LỖI] UID hoặc Username không được để trống!")
        return

    fetch_token = input("  > Nhập RevenueCat Fetch Token: ").strip()
    if not fetch_token:
        print("[❌ LỖI] Fetch Token không được để trống!")
        return

    app_transaction = input("  > Nhập App Transaction (Receipt): ").strip()
    if not app_transaction:
        print("[❌ LỖI] App Transaction không được để trống!")
        return

    nextdns_key = input("  > Nhập NextDNS API Key (Nhấn Enter nếu không dùng): ").strip()
    if not nextdns_key:
        nextdns_key = None

    print("\n" + "-" * 65)
    print("[⏳] Đang tiến hành xử lý yêu cầu...")

    activator = LocketActivator(nextdns_key=nextdns_key)
    
    # Xử lý tạo NextDNS nếu người dùng có nhập key
    if nextdns_key:
        print("[⚙️] Đang tạo NextDNS Profile bảo vệ...")
        profile_id = await activator.create_nextdns_profile(target_uid)
        if profile_id:
            print(f"[✅] Đã tạo thành công NextDNS Profile ID: {profile_id}")
        else:
            print("[⚠️] Không thể tạo NextDNS profile, tiếp tục tiến trình kích hoạt...")

    # Gửi request kích hoạt chính thức
    success, message = await activator.activate_gold(target_uid, fetch_token, app_transaction)

    print("-" * 65)
    if success:
        print(f"[🎉 THÀNH CÔNG] {message}")
    else:
        print(f"[❌ THẤT BẠI] {message}")
    print("=" * 65)

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
