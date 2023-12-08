from __future__ import annotations

from langchain_benchmarks.schema import ModelRegistry, RegisteredModel

_OpenAIModels = [
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-1106",
        type="chat",
        description=(
            "The latest GPT-3.5 Turbo model with improved instruction following, "
            "JSON mode, reproducible outputs, parallel function calling, and more. "
            "Returns a maximum of 4,096 output tokens."
        ),
        params={
            "model": "gpt-3.5-turbo-1106",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo",
        type="chat",
        description="Currently points to gpt-3.5-turbo-0613.",
        params={
            "model": "gpt-3.5-turbo",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-16k",
        type="chat",
        description="Currently points to gpt-3.5-turbo-0613.",
        params={
            "model": "gpt-3.5-turbo-16k",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-instruct",
        type="llm",
        description=(
            "Similar capabilities as text-davinci-003 but compatible with legacy "
            "Completions endpoint and not Chat Completions."
        ),
        params={
            "model": "gpt-3.5-turbo-instruct",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-0613",
        type="chat",
        description=(
            "Legacy Snapshot of gpt-3.5-turbo from June 13th 2023. "
            "Will be deprecated on June 13, 2024."
        ),
        params={
            "model": "gpt-3.5-turbo-0613",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-16k-0613",
        type="chat",
        description=(
            "Legacy Snapshot of gpt-3.5-16k-turbo from June 13th 2023. "
            "Will be deprecated on June 13, 2024."
        ),
        params={
            "model": "gpt-3.5-turbo-16k-0613",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="gpt-3.5-turbo-0301",
        type="chat",
        description=(
            "Legacy Snapshot of gpt-3.5-turbo from March 1st 2023. "
            "Will be deprecated on June 13th 2024."
        ),
        params={
            "model": "gpt-3.5-turbo-0301",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="text-davinci-003",
        type="llm",
        description=(
            "Legacy Can do language tasks with better quality and consistency than "
            "the curie, babbage, or ada models. Will be deprecated on Jan 4th 2024."
        ),
        params={
            "model": "text-davinci-003",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="text-davinci-002",
        type="llm",
        description=(
            "Legacy Similar capabilities to text-davinci-003 but trained with "
            "supervised fine-tuning instead of reinforcement learning. "
            "Will be deprecated on Jan 4th 2024."
        ),
        params={
            "model": "text-davinci-002",
        },
    ),
    RegisteredModel(
        provider="openai",
        name="code-davinci-002",
        type="llm",
        description="Legacy Optimized for code-completion tasks. Will be deprecated "
        "on Jan 4th 2024.",
        params={
            "model": "code-davinci-002",
        },
    ),
]

_FireworksModels = [
    RegisteredModel(
        provider="fireworks",
        name="llama-v2-7b-chat-fw",
        type="chat",
        description="7b parameter LlamaChat model",
        params={
            "model": "accounts/fireworks/models/llama-v2-7b-chat",
        },
    ),
    RegisteredModel(
        provider="fireworks",
        name="llama-v2-13b-chat-fw",
        type="chat",
        description="13b parameter LlamaChat model",
        params={
            "model": "accounts/fireworks/models/llama-v2-13b-chat",
        },
    ),
    RegisteredModel(
        provider="fireworks",
        name="llama-v2-70b-chat-fw",
        type="chat",
        description="70b parameter LlamaChat model",
        params={
            "model": "accounts/fireworks/models/llama-v2-70b-chat",
        },
    ),
]

model_registry = ModelRegistry(registered_models=_OpenAIModels + _FireworksModels)
