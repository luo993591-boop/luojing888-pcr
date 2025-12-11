import json
import random
from datetime import datetime

def gen_pcr():
    """模拟一个合理区间的PCR值（0.60～1.40）"""
    return round(random.uniform(0.60, 1.40), 3)

# 5大指数
indices = {
    "上证指数": gen_pcr(),
    "深证成指": gen_pcr(),
    "沪深300": gen_pcr(),
    "创业板": gen_pcr(),
    "科创50": gen_pcr(),
}

data = {
    "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "pcr": indices
}

with open("pcr_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("PCR 数据已自动生成并写入 pcr_data.json")
