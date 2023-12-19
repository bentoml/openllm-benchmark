from common import start_benchmark_session, get_prompt_set
import asyncio
import json


class UserDef:
    BASE_URL = "http://1.2.3.4:3000"

    @classmethod
    def ping_url(cls):
        return f"{cls.BASE_URL}/healthz"

    @classmethod
    def make_request(cls):
        """
        return url, headers, body
        """
        import openllm
        import json
        import random

        prompt = random.choice(get_prompt_set(15, 25))

        headers = {"accept": "application/json", "Content-Type": "application/json"}
        config = (
            openllm.AutoConfig.for_model("llama")
            .model_construct_env(max_new_tokens=20, top_p=0.21)
            .model_dump()
        )
        data = {"prompt": prompt, "llm_config": config, "adapter_name": None}
        url = f"{cls.BASE_URL}/v1/generate_stream"
        return url, headers, json.dumps(data)

    @classmethod
    def parse_response(cls, chunk):
        """
        take chunk and return list of tokens, used for token counting
        """
        data = chunk.decode()[6:]
        if "[DONE]" in data:
            return
        try:
            return json.loads(data)["outputs"][0]["token_ids"]
        except json.JSONDecodeError as err:
            return

    @staticmethod
    async def rest():
        import asyncio

        await asyncio.sleep(0.01)


if __name__ == "__main__":
    asyncio.run(start_benchmark_session(UserDef))
