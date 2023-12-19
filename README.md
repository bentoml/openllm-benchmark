# Preparing the environment

```
pip install openllm==0.4.35
```

# benchmark OpenLLM
1.

```bash
openllm start meta-llama/Llama-2-7b-hf --backend vllm
```

2.
Edit openllm_llama2_20_prompt.py to set the correct base url to the OpenLLM server.


3.
```bash
python openllm_llama2_20_prompt.py --max_users 1 --session_time 300 --ping_correction
```

