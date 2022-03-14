# tooltrade
run: python trade_menu.py
# convert py to exe:
pyinstaller --onefile -w trade_menu.py

# Lưu ý:

Tùy theo từng coin, sàn mà thay đổi ở file trade.py và trade_detail.py
transaction_fee là phí giao dịch của sàn đang dùng
set chênh lệch giá cho price_buy tùy theo từng coin:
``
for price_buy in np.arange(price_sell , price_sell-0.05, -0.0001)[1:]:
``
set số lượng lời tùy lòng tham:
``
for j in np.arange(5, 20, 5):
``
