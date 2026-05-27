from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import pyautogui
import pyperclip
import time

# =========================
# 启动 Edge
# =========================

driver = webdriver.Edge(service=Service())

# =========================
# 打开 Outlook
# =========================

driver.get("https://outlook.office.com/mail/")

print("等待 Outlook 加载...")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[role="option"]')
    )
)

# 等待邮件完全加载
time.sleep(5)

# =========================
# 获取第一页邮件
# =========================

emails = driver.find_elements(
    By.CSS_SELECTOR,
    '[role="option"]'
)

# =========================
# 存储邮件
# =========================

mail_list = []

print("\n====== 最新邮件 ======\n")

count = 0

# =========================
# 遍历邮件
# =========================

for email in emails:

    try:

        # 最多读取前10封
        if count >= 10:
            break

        lines = email.text.split("\n")

        # =========================
        # 跳过固定邮件
        # =========================

        is_pinned = False

        for line in lines:

            if "\ue89e" in line:

                is_pinned = True

        if is_pinned:
            continue

        # =========================
        # 清洗文本
        # =========================

        clean_lines = []

        for line in lines:

            line = line.strip()

            if line != "":

                clean_lines.append(line)

        # 内容太少跳过
        if len(clean_lines) < 2:
            continue

        # =========================
        # 删除无用字段
        # =========================

        useful_lines = []

        for line in clean_lines:

            # 跳过短缩写
            if len(line) <= 3:
                continue

            # 跳过奇怪图标
            strange = False

            for c in line:

                if ord(c) > 50000:

                    strange = True

            if strange:
                continue

            useful_lines.append(line)

        # 至少需要 sender + title
        if len(useful_lines) < 2:
            continue

        # =========================
        # 提取发件人和标题
        # =========================

        sender = useful_lines[0]
        title = useful_lines[1]

        # =========================
        # 输出调试
        # =========================

        print(f"发件人：{sender}")
        print(f"标题：{title}")
        print("--------------------")

        # =========================
        # 保存邮件
        # =========================

        mail_info = f"""
发件人：{sender}
标题：{title}
"""

        mail_list.append(mail_info)

        count += 1

    except:
        pass

# =========================
# 生成 Prompt
# =========================

prompt = """
请帮我总结以下 Outlook 邮件。

要求：
1. 按重要程度分类
2. 提醒我哪些可能需要处理
3. 用简洁中文总结
4. 忽略明显不重要通知

邮件内容：

"""

for mail in mail_list:

    prompt += mail

# =========================
# 保存 TXT
# =========================

with open("mail_summary.txt", "w", encoding="utf-8") as f:

    f.write(prompt)

print("\n邮件内容已保存到 mail_summary.txt")

# =========================
# 打开豆包
# =========================

subprocess.Popen(
    r"D:\LenovoSoftstore\Install\doubao\Doubao.exe"
)

print("正在打开豆包...")

# 等待豆包启动
time.sleep(8)

# =========================
# 点击豆包输入框
# =========================

pyautogui.click(895, 1257)

time.sleep(1)

# =========================
# 粘贴 Prompt
# =========================

pyperclip.copy(prompt)

pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# =========================
# 回车发送
# =========================

pyautogui.press("enter")

print("已发送到豆包")

# =========================
# 关闭 Outlook
# =========================

driver.quit()

print("Outlook 已关闭，仅保留豆包")
