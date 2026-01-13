from openai import OpenAI

# 配置Ollama服务器连接
openai_api_key = "ollama"  # Ollama不需要实际的API密钥，但openai库需要一个值
openai_api_base = "http://43.156.133.9:80/v1"  # 您提供的Ollama服务器地址

# 初始化客户端
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# 设置查询内容
prompt = "我检测出来胆碱高，应该怎么办？"

try:
    # 发送请求到指定模型
    response = client.chat.completions.create(
        model="./qwen25-14b-unsloth-finetuned-bnb-4bit/",
        messages=[
            {"role": "user", "content": "你是一个专业的医疗健康顾问，能够提供有关体检指标异常的专业建议。"+ prompt},
        ],
        stream=False,
        temperature=0.7,
        max_tokens=500
    )
    
    # 输出模型的回答
    print("关于胆碱偏高的处理建议：")
    print(response.choices[0].message.content)
    
except Exception as e:
    print(f"请求过程中发生错误: {e}")
