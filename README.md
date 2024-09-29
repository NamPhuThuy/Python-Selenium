# Python-Selenium  

## Note
Check the version of the using Browser:
Download Chrome driver with the same version:
- Chrome:	 https://sites.google.com/chromium.org/driver/
- Edge:	 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Firefox: https://github.com/mozilla/geckodriver/releases
- Safari:	 https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Selenium version: 4.14.0


## Differ between driver.close() & driver.quit()

| Feature| driver.quit()| driver.close()|
|-----------------------------------|--------------------------------|--------------------------------|
| Behaviour:| Đóng tất cả cửa sổ browser liên kết tới WebDriver session| Chỉ đóng focused window hiện tại|
| Impact:| Tài nguyên được giải phóng, ngăn **memory leaks**, WebDriver được tắt đúng cách | Tài nguyên không được giải phóng, có thể xảy ra memory leaks, WebDriver session vẫn active |
| Usage:| Thường được gọi ở cuối Selenium script để dọn dẹp tài nguyên| Dùng để đóng cửa sổ hiện tại|
