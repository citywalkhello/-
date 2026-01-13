from evalscope import TaskConfig, run_task
import os

print("原始工作路径:", os.getcwd())
os.chdir("/workspace/")
print("新工作路径:", os.getcwd())

task_cfg = TaskConfig(
    model='model/',
    datasets=['general_qa'],  # 数据格式，问答题格式固定为 'general_qa'
    dataset_args={
        'general_qa': {
            "local_path": "qa",  # 自定义数据集路径
            "subset_list": [
                # 评测数据集名称，上述 *.jsonl 中的 *，可配置多个子数据集
                "med"       
            ]
        }
    },
)

run_task(task_cfg=task_cfg)