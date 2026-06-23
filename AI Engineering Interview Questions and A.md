AI Engineering Interview Questions and Answers
AI Engineering Interview Questions and Answers - Your Cheat Sheet For AI Engineering Interviews

These interview questions and answers are helpful for roles such as:

AI Engineer
Gen AI Engineer
LLM Engineer
Agentic AI Engineer
AI Agent Engineer
AI Solutions Architect
AI Platform Engineer
Applied AI Engineer
MLOps Engineer
LLMOps Engineer
Table of Contents
Must Know
LLM Fundamentals
Prompt Engineering
Retrieval-Augmented Generation (RAG)
AI Agents and Agentic Systems
Fine-Tuning and Model Adaptation
Vector Databases and Embeddings
AI System Design
LLMOps and Production AI
Evaluation and Testing
AI Safety, Ethics, and Responsible AI
Multimodal AI
AI Infrastructure and Scalability
Coding and Practical Implementation
Behavioral and Scenario-Based Questions
LangChain
LangGraph
Python
FastAPI
Resume-Based Questions
System Design & Scenario-Based
Prepared and maintained by the Founder of Outcome School: Amit Shekhar
Follow Amit Shekhar
X/Twitter
LinkedIn
GitHub
Follow Outcome School
YouTube
X/Twitter
LinkedIn
GitHub
I teach at Outcome School
AI and Machine Learning
Note: We will keep updating this with new questions and answers.

Must Know
LLM
RAG
MCP
Agent
Fine-tuning
Quantization
Learn about the LLM, RAG, MCP, Agent, Fine-tuning & Quantization: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization

LLM Fundamentals
What are foundation models, and how have they changed AI engineering?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is a Large Language Model (LLM), and how does it work?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
Inside ChatGPT: What Happens After You Hit Enter?
Answer: Inside ChatGPT: What Happens After You Hit Enter
What is the Transformer architecture and how does it work?
Answer: Decoding Transformer Architecture
What are the key components of the Transformer architecture?
Answer: Decoding Transformer Architecture
What is tokenization in LLMs?
Answer: Tokenization in Large Language Models (LLMs)
Explain BPE (Byte Pair Encoding).
Answer: Byte Pair Encoding
Explain WordPiece and SentencePiece.
What is positional encoding, and why is it needed in Transformers?
Answer: Positional Embeddings in LLMs
What are embeddings?
Answer: Embeddings in Machine Learning
Explain the Query(Q), Key(K), and Value(V) in attention.
Answer: Math behind Attention - Q, K, and V
What is self-attention, and how does it work in Transformers?
Answer: Self Attention in Transformers
What is Cross Attention in Transformers?
Answer: Cross Attention in Transformers
Why do we scale the dot product attention by √dₖ in the Transformer architecture?
Answer: Math behind √dₖ Scaling Factor in Attention
What is causal masking?
Answer: Causal Masking in Attention
What are multi-head attention mechanisms? Why use multiple attention heads?
Answer: Multi-Head Attention in Transformers
What are Feed-Forward Networks in LLMs?
Answer: Feed-Forward Networks in LLMs
What is the context window in LLMs, and why does it matter?
Answer: Context Window in LLMs
Why is the context window limited in LLMs?
Answer: Why is the context window limited in LLMs?
What is temperature in the context of LLMs, and how does it affect output?
Answer: What is temperature in the context of LLMs?
Why is the first token slower than the rest in an LLM?
Answer: The First-Token Latency Problem in LLMs
Explain Top-p (nucleus) sampling and Top-k sampling. How do they differ?
What are logits, and how are they used in text generation?
Answer: Understanding Logits in Machine Learning
What are skip connections (residual connections) in Transformers?
Answer: Skip connections (residual connections) in Transformers
What is the difference between open-source and closed-source LLMs? When would you choose one over the other?
What is the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures?
Answer: Decoding Transformer Architecture
What is KV cache, and how does it speed up inference?
Answer: What is KV Cache in LLMs?
What is model distillation, and how is it used with LLMs?
Answer: How does Knowledge Distillation work?
What is Mixture of Experts (MoE), and how does it work in models like Mixtral?
Answer: Mixture of Experts Explained
What is the difference between dense and sparse models?
Answer: Mixture of Experts Explained
What is Flash Attention?
Answer: Decoding Flash Attention in LLMs
What is Cross-Entropy Loss?
Answer: Math Behind Cross-Entropy Loss
What is Grouped-Query Attention (GQA), and how does it differ from Multi-Head Attention (MHA)?
Answer: Grouped Query Attention
How does Rotary Position Embedding (RoPE) work, and why is it preferred over learned positional embeddings?
Answer: Math Behind RoPE (Rotary Position Embedding)
Explain Layer Normalization
Answer: Batch Normalization vs Layer Normalization
Explain RMSNorm (Root Mean Square Layer Normalization)
Answer: RMSNorm (Root Mean Square Layer Normalization)
Your LLM keeps ignoring your instructions. How do you make it follow structured output formats?
Your LLM-powered tool hits the context window limit on long documents. How do you handle it?
Your LLM does not admit when it does not know the answer. How do you make it say "I don't know"?
Your LLM generates responses that are too verbose. How do you control response length?
Your LLM memorized proprietary training data and leaks it in responses. How do you prevent this?
Your LLM coding assistant generates outdated code using deprecated libraries. How do you fix it?
Your tokenizer splits important domain terms into meaningless subword pieces. How do you fix it?
Your Transformer's KV cache grows too large during long sequence generation. How do you manage memory?
Answer: Paged Attention in LLMs
Your Transformer runs out of memory on long documents due to quadratic self-attention. How do you scale it?
Your distilled student model fails on the complex reasoning that the teacher model handled. How do you close the gap?
After RLHF alignment, your LLM became safer but lost capability on hard tasks. How do you manage the alignment tax?
Your RLHF-trained LLM is gaming the reward model instead of being genuinely helpful. How do you fix reward hacking?
Answer: Reinforcement Learning from Human Feedback (RLHF)
Your chatbot loses context after 10 turns in a conversation. How do you maintain a long conversation context?
Your chatbot fails when users switch topics mid-conversation. How do you handle topic switches?
Your QA system always generates an answer even when no answer exists in the context. How do you detect unanswerable questions?
Your summarization system hallucinated facts not in the original article. How do you fix it?
Your text generation repeats phrases in long outputs. How do you fix repetition?
Transformers work on text, so can they also understand images?
Answer: Decoding Vision Transformer (ViT)
Small Language Models (SLMs)
Answer: Small Language Models (SLMs)
Large Reasoning Models (LRMs)
Answer: Large Reasoning Models (LRMs)
What are Autoregressive Models?
Answer: Autoregressive Models
Explain the difference between autoregressive and masked language modeling.
Proximal Policy Optimization (PPO)
Answer: Proximal Policy Optimization (PPO)
Direct Preference Optimization (DPO)
Answer: Direct Preference Optimization (DPO)
Group Relative Policy Optimization (GRPO)
Answer: Group Relative Policy Optimization (GRPO)
Recursive Language Models (RLMs)
Answer: Recursive Language Models (RLMs)
Continual Learning in LLMs
Answer: Continual Learning in LLMs
Prompt Engineering
What is prompt engineering, and why is it critical for AI applications?
Explain zero-shot, one-shot, and few-shot prompting with examples.
Answer: Explain zero-shot, one-shot, and few-shot prompting with examples
What is chain-of-thought (CoT) prompting, and when should you use it?
Explain self-consistency prompting and how it improves reasoning.
What is tree-of-thought prompting?
What is ReAct (Reasoning + Acting) prompting, and how does it work?
Answer: ReAct Agent
What is a system prompt, and how does it influence model behavior?
How do you structure prompts for consistent structured output (JSON, XML)?
What is prompt injection, and how do you defend against it?
What is jailbreaking in LLMs, and what are common jailbreak techniques?
How do you optimize prompts for cost and latency?
What is the difference between prompt engineering and prompt tuning?
What is a prompt template, and how do you design one for production use?
How do you handle multi-turn conversations with LLMs?
What is role prompting, and when is it effective?
What is prompt chaining, and how do you design a chain of prompts for complex tasks?
How do you evaluate and iterate on prompt quality?
What are meta-prompts, and how can they be used to generate prompts?
What are the common failure modes in prompting, and how do you debug them?
How do you handle edge cases and adversarial inputs in prompt design?
What is the "lost in the middle" problem in long-context prompting?
What are output parsers, and why are they needed for production applications?
How do you handle multi-language prompting effectively?
Your few-shot prompting gives inconsistent results across similar inputs. How do you stabilize it?
Your LLM classification system is too sensitive to prompt wording changes. How do you reduce prompt sensitivity?
Your chatbot's system prompt containing proprietary business logic is being leaked by users. How do you prevent it?
Your LLM agent is vulnerable to prompt injection that reveals the system prompt. How do you defend it?
Your chain-of-thought prompting is not improving LLM accuracy on reasoning tasks. What do you fix?
Your AI system works in English but fails for other languages. How do you add multilingual support?
Your zero-shot cross-lingual transfer from English fails on other languages. How do you fix it?
Retrieval-Augmented Generation (RAG)
What is Retrieval-Augmented Generation (RAG), and why is it important?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
Explain the architecture of a basic RAG system.
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What are the key components of a RAG pipeline?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What are chunking strategies, and how do you choose the right chunk size?
Compare fixed-size chunking, semantic chunking, and recursive chunking.
What are embedding models, and how do they convert text to vectors?
How do you choose an embedding model for your RAG system?
Explain Agentic RAG.
Answer: Agentic RAG
What is hybrid search, and why is it better than pure vector search?
What is re-ranking, and how does it improve RAG retrieval quality?
Answer: How does a Reranker work?
How do you handle multi-document and multi-hop questions in RAG?
What is the "lost in the middle" problem in RAG systems?
How do you evaluate a RAG system? Explain faithfulness, relevance, and context precision/recall.
Explain Self-RAG. How does the model decide when to retrieve?
What is GraphRAG, and when would you use it over traditional RAG?
Answer: GraphRAG
How do you handle structured data (tables, SQL databases) in a RAG pipeline?
What are the common failure modes of RAG systems, and how do you debug them?
How do you handle document updates and maintain freshness in a RAG system?
How do you optimize RAG for latency in production?
What is the role of metadata filtering in RAG systems?
Compare RAG vs fine-tuning. When would you use each?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is query transformation in RAG (HyDE, query decomposition, step-back prompting)?
How do you implement citation and source attribution in RAG?
How do you scale a RAG system to millions of documents?
What is parent-child chunking, and how does it improve retrieval?
Your RAG system is hallucinating despite having the right context. How do you fix it?
Your RAG chunk overlap causes redundant results. How do you reduce redundancy?
Your RAG retrieval is too slow with a large knowledge base. How do you speed it up?
Your RAG system returns duplicate results. How do you deduplicate?
Your RAG system needs per-user access control on internal documents. How do you implement it?
Your RAG system fails on domain-specific jargon. How do you fix it?
Your text-only RAG system now needs to handle images and tables. How do you extend it?
Your RAG knowledge base gets updated frequently and needs versioning. How do you manage it?
Your RAG system fails on multi-hop questions that require combining multiple facts. How do you fix it?
Your enterprise RAG system returns contradictory answers from different source documents. How do you resolve conflicts?
Your RAG system returns outdated answers from an evolving knowledge base. How do you keep it current?
Your RAG system struggles with PDF documents containing tables and layouts. How do you fix PDF parsing?
AI Agents and Agentic Systems
What is an AI agent, and how does it differ from a simple LLM call?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization and AI Agent Explained
AI Agent Memory
Answer: AI Agent Memory
Harness Engineering in AI
Answer: Harness Engineering in AI
Explain the ReAct (Reasoning + Acting) agent architecture.
Answer: ReAct Agent
What is the Plan-and-Execute agent pattern?
Answer: Plan-and-Execute Agent
What is tool use (function calling) in LLMs, and how does it enable agents?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
How do you design and define tools for an AI agent?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is the difference between single-agent and multi-agent systems?
Answer: Multi-Agent Systems
What is Model Context Protocol (MCP), and how does it standardize tool integration?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What are AI SubAgents?
Answer: AI SubAgents
What are the different types of agent memory (short-term, long-term, episodic)?
How do you handle agent failures and implement error recovery?
What is an agent loop, and how does it decide when to stop?
Answer: AI Agent Loop
Context Engineering
Answer: Context Engineering
How AI Agents Communicate?
Answer: How AI Agents Communicate
How do you evaluate and test AI agents?
Answer: AI Agent Evaluation
What are the security risks of agentic systems, and how do you mitigate them?
What is the difference between reactive and proactive agents?
How do you manage token consumption and cost in long-running agent workflows?
What is the human-in-the-loop pattern for agents, and when is it needed?
How do you implement guardrails for AI agents to prevent harmful actions?
What is agent reflection, and how does it improve agent performance?
Answer: Reflection Agent
What is the difference between code-generating agents and tool-calling agents?
How do you handle multi-modal inputs and outputs in agentic systems?
How do you implement state management in complex agent workflows?
How do you build a customer support agent with escalation logic?
What is agent orchestration, and how do you implement it?
Answer: AI Orchestration
How do you build a code execution agent safely using sandboxed environments?
Your AI agent is stuck in an infinite loop. How do you detect and break the cycle?
Answer: Fix an infinite loop in an AI agent
Your AI agent gets conflicting answers from different tools. How does it reconcile them?
Your AI agent burns too many tokens per task. How do you reduce token consumption?
Answer: How would you reduce the token consumption?
Your AI agent keeps exceeding its budget per task. How do you enforce budget limits?
Your AI agent hallucinates tool capabilities and passes wrong inputs. How do you fix it?
Your AI agent deleted a production database. How do you prevent irreversible actions?
Your AI agent has many tools, but keeps picking the wrong one. How do you improve tool selection?
Your AI agent takes too long to complete a task. How do you speed it up?
Your LLM selects the right tool but extracts the wrong parameters. How do you fix parameter extraction?
Fine-Tuning and Model Adaptation
What is fine-tuning, and when should you fine-tune an LLM?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
Explain the difference between full fine-tuning and parameter-efficient fine-tuning (PEFT).
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is LoRA (Low-Rank Adaptation), and how does it work?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is QLoRA, and how does it enable fine-tuning on consumer hardware?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
Explain Prefix Tuning and Prompt Tuning. How are they different from LoRA?
What is adapter-based fine-tuning?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
What is RLHF (Reinforcement Learning from Human Feedback), and how is it used to align LLMs?
Answer: Reinforcement Learning from Human Feedback (RLHF)
What is instruction tuning, and why is it important for chat models?
How do you prepare a dataset for fine-tuning an LLM?
What is catastrophic forgetting, and how do you prevent it during fine-tuning?
When should you choose fine-tuning over RAG over prompt engineering?
How do you evaluate a fine-tuned model's performance?
What is synthetic data generation, and how do you use it for fine-tuning?
What are the key hyperparameters for fine-tuning (learning rate, epochs, batch size, LoRA rank)?
Answer: LoRA - Low-Rank Adaptation of LLMs
How do you fine-tune a model for a specific domain (legal, medical, finance)?
What is continual pre-training, and when would you use it?
How do you merge multiple LoRA adapters?
Answer: LoRA - Low-Rank Adaptation of LLMs
What is the difference between SFT (Supervised Fine-Tuning) and alignment training?
What is RLAIF (RL from AI Feedback), and how does it differ from RLHF?
What is knowledge distillation for fine-tuning, and what are the legal considerations?
Answer: How does Knowledge Distillation work?
Your fine-tuned LLM produces factually wrong outputs due to training data quality issues. How do you fix it?
You must choose between LoRA and full fine-tuning for a domain-specific assistant. How do you decide?
Answer: LoRA - Low-Rank Adaptation of LLMs
Your fine-tuned model memorized training data verbatim instead of learning patterns. How do you fix overfitting?
Your fine-tuned LLM forgot its general capabilities after domain-specific fine-tuning. How do you fix catastrophic forgetting?
Your RLHF preference data has low annotator agreement. How do you ensure data quality?
Vector Databases and Embeddings
What are embeddings in the context of AI engineering?
Answer: Embeddings in Machine Learning
How do embedding models convert text to vectors?
What is the difference between sparse and dense embeddings?
Explain cosine similarity, dot product, and Euclidean distance for vector search.
Answer: How does a Vector Database work?
What is a vector database, and how does it differ from a traditional database?
Answer: How does a Vector Database work?
How do you choose the right embedding model for your use case?
What is embedding dimensionality, and how does it affect performance and cost?
How do you handle embedding drift when the embedding model is updated?
What are multi-modal embeddings, and how are they generated?
How do you index and query multi-tenant data in a vector database?
What is quantization of embeddings, and how does it reduce storage costs?
How do you benchmark and evaluate embedding model quality?
What is the role of metadata in vector databases?
Answer: How does a Vector Database work?
How do you handle large-scale vector search with billions of vectors?
What is hybrid search (combining keyword search with vector search)?
How do you fine-tune an embedding model for a specific domain?
Your vector database for RAG is consuming too much memory. How do you reduce it?
Your vector database cannot scale to millions of embeddings. How do you fix the bottleneck?
Your new embedding model has different dimensions from the existing vectors in production. How do you handle the mismatch?
Your vector search returns irrelevant results despite high similarity scores. How do you fix it?
You deployed a new embedding model, and search quality crashed overnight. How do you handle embedding drift?
Your semantic search fails for short queries. How do you improve it?
AI System Design
Design ChatGPT: Training to Serving (End to End)
Design a RAG System (Chat with Your Documents)
Design Memory for a Personal AI Assistant
Design a Deep Research Agent
Design a Multi-Agent Customer Support System
Design an On-Device AI Assistant
Design a Multimodal Search System (Text, Image, Video)
Design an LLM Inference Platform (vLLM-as-a-Service)
Design an LLM Evaluation Platform
Design a Text-to-Image Generation Service (Midjourney-like)
Design a Music Generation Service (Suno-like)
Design a Video Generation Service (Sora-like)
Design an AI Coding Agent.
Design a code generation and review system.
Design a content moderation system using AI.
Design a real-time AI recommendation system.
Design an AI-powered email assistant.
Design a medical diagnosis assistant using AI.
Design a fraud detection system powered by LLMs.
Design an AI-powered data extraction pipeline from unstructured documents.
Design a personalized learning assistant.
Design an AI system for automated code migration.
Design an AI-powered legal document review system.
Design a conversational AI system with memory across sessions.
How do you design for latency vs quality trade-offs in AI systems?
How do you implement caching strategies for LLM applications?
How do you design rate limiting and cost management for AI APIs?
How do you handle failover and fallback strategies for AI systems?
How do you design an AI system for high availability and fault tolerance?
How do you design an AI system that gracefully degrades when the model is unavailable?
What are the key considerations for multi-region deployment of AI systems?
Design an AI-powered search engine for an e-commerce platform.
Design an AI gateway/proxy for managing LLM access across an organization.
How do you design a RAG system that handles conflicting information across sources?
How do you approach capacity planning for an AI system?
Design a multi-tenant AI chatbot platform where each business gets a custom chatbot.
Design an AI meeting summarizer system for thousands of meetings daily.
Design an AI notification system that prioritizes instead of broadcasting.
Design an AI-powered anomaly detection system for cloud infrastructure.
Design an AI-powered document processing pipeline for financial institutions.
Design an AI dynamic pricing engine.
Design an AI resume screening system that handles 100K applications per week.
Design an AI voice assistant architecture.
Design a multi-agent workflow system where agents collaborate on complex tasks.
Answer: Multi-Agent Systems
Design a real-time AI transcription system for concurrent audio streams.
Design an AI-powered live streaming content moderation system.
LLMOps and Production AI
How does Prompt Caching work?
Answer: How does Prompt Caching work?
Explain the AI product lifecycle from ideation to production.
What is LLMOps, and how does it differ from traditional MLOps?
How do you serve LLMs in production?
What is model quantization?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
How do you monitor LLM applications in production?
What is LLM observability?
What are guardrails for LLMs, and how do you implement them?
How do you implement content filtering for AI outputs?
How do you estimate the cost of running an AI-powered feature in production?
How do you optimize LLM inference costs in production?
How do you implement A/B testing for LLM systems?
What is CI/CD for AI applications, and how does it differ from traditional CI/CD?
How do you version and manage prompts in production?
What is model versioning, and how do you handle model rollbacks?
How do you implement rate limiting and throttling for LLM APIs?
How do you handle model updates and migrations without downtime?
What is the role of feature flags in AI deployments?
How do you implement logging and tracing for LLM applications?
How do you handle PII and sensitive data in LLM inputs and outputs?
What is a gateway pattern for LLM API management?
How does Token Streaming work?
Answer: How does Token Streaming work?
How do you implement streaming responses for real-time AI applications?
Answer: How does Token Streaming work?
What are the key SLAs and metrics for production AI systems (latency, throughput, availability)?
Cloud vs on-device Model Deployment for AI applications.
Answer: Cloud vs On-Device Model Deployment
How do you implement fallback strategies when the primary model is unavailable or rate-limited?
How do you implement structured output from LLMs reliably in production?
How do you handle long contexts efficiently in production (context compression, prefix caching)?
What is semantic routing, and how do you implement it in a multi-model system?
How do you manage secrets and API keys securely in LLM applications?
Your LLM API has latency spikes during peak hours. How do you stabilize it?
Your LLM costs are too high in production. How do you reduce costs without degrading quality?
Your application is hitting LLM provider rate limits during peak hours. How do you handle it?
Your application depends on one LLM provider. How do you switch providers without downtime?
Your AI system handles 100 requests/sec but crashes at 5000. How do you scale for concurrent requests?
A traffic spike brings down your AI system. How do you handle peak traffic?
One LLM provider outage took down your entire system. How do you eliminate single points of failure?
Your multi-LLM pipeline fails when one model in the chain breaks. How do you handle orchestration failure?
Answer: AI Orchestration
Your AI pipeline has zero visibility into which step is failing. How do you add observability?
You quantized your LLM, but accuracy dropped significantly. How do you minimize quantization loss?
One failing AI component can take down your entire platform. How do you design graceful degradation?
Evaluation and Testing
AI Agent Evaluation
Answer: AI Agent Evaluation
LLM Evaluation
Answer: LLM Evaluation
AI Agent Observability
Answer: AI Agent Observability
What is evaluation-driven development for AI applications?
How do you evaluate LLM outputs? What metrics do you use?
Explain BLEU, ROUGE, and BERTScore. When would you use each?
What is G-Eval, and how does it use LLMs for evaluation?
What is LLM-as-a-judge evaluation, and what are its limitations?
Answer: LLM as a Judge
How do you conduct human evaluation for AI systems?
What is red teaming, and how do you red team an LLM application?
How do you detect and measure hallucinations in LLM outputs?
What is adversarial testing for AI systems?
How do you build a regression test suite for AI applications?
What are benchmark suites (MMLU, HumanEval, GSM8K), and how do you interpret them?
How do you evaluate a RAG system end-to-end?
How do you evaluate the quality of AI agents?
What is the difference between offline and online evaluation for AI systems?
How do you measure factual consistency in LLM outputs?
How do you evaluate multi-turn conversation quality?
What is the role of golden datasets in AI evaluation?
How do you implement continuous evaluation for production AI systems?
How do you evaluate bias in AI model outputs?
How do you compare two models or prompts in a statistically rigorous way?
How do you evaluate the robustness of an LLM application across input variations?
What are the key differences between evaluating traditional ML vs LLM applications?
How do you set up an evaluation framework from scratch for a new LLM application?
Your model passes one fairness metric but fails another. How do you handle conflicting audit results?
Your model was fair at deployment, but became biased 6 months later. How do you monitor continuously?
An external auditor cannot reproduce your model's results. How do you ensure audit reproducibility?
How do you structure red teaming for an LLM chatbot before launch?
How do you red team a multimodal model where text-only safety tests miss cross-modal attacks?
AI Safety, Ethics, and Responsible AI
What are hallucinations in LLMs, and how do you mitigate them?
What is prompt injection, and what are the different types (direct, indirect)?
How do you implement input and output guardrails for AI systems?
What is AI alignment, and why is it important?
How do you detect and mitigate bias in AI systems?
What are the key data privacy considerations (GDPR, CCPA) when building AI applications?
How do you handle PII in LLM inputs and outputs?
What is explainability in AI, and why does it matter?
What is the difference between interpretability and explainability?
How do you build trust with users in AI-powered applications?
What are adversarial attacks on AI systems, and how do you defend against them?
What is data poisoning, and how can it affect AI models?
How do you implement content safety filters for AI-generated content?
What is responsible AI, and what frameworks exist for implementing it?
How do you handle copyright and intellectual property concerns with AI-generated content?
What is the EU AI Act, and how does it affect AI engineering?
How do you implement audit trails and logging for AI decisions?
What is model card documentation, and why is it important?
How do you handle misuse and abuse of AI systems in production?
What is differential privacy, and how can it be applied during model training?
How would you design an AI incident response plan?
What is the NIST AI Risk Management Framework (AI RMF)?
Your healthcare chatbot gives medical diagnoses it should not make. How do you add safety guardrails?
Your AI system is reproducing copyrighted material verbatim. How do you prevent this?
Your resume screening AI rejects more female candidates for engineering roles. How do you fix gender bias?
Your AI model passes bias checks by gender and race separately, but fails for intersectional groups. How do you handle it?
Your AI denied a loan, and the customer demands a GDPR explanation. How do you provide one?
A user invokes the right to be forgotten, but their data is in your model weights. How do you comply?
The EU AI Act may classify your AI system as high-risk. How do you comply?
Your differentially private model lost significant accuracy. How do you balance privacy and utility?
One malicious participant is poisoning your federated learning model. How do you defend against it?
Your AI hiring model uses proxy features for protected attributes. How do you eliminate proxy discrimination?
Your predictive model creates a feedback loop of biased outcomes. How do you break it?
Your AI generates fake news images. How do you implement watermarking for AI-generated content?
Your AI denies a service, and the user has no way to challenge it. How do you design an appeals process?
An auditor asks why your AI rejected a request 6 months ago, and you have no logs. How do you build audit trails?
You removed PII, but users were re-identified from anonymized data. How do you prevent re-identification?
A pre-trained model from an open-source repo may contain a hidden backdoor. How do you detect it?
Your LLM's training data was deliberately poisoned by an adversary. How do you respond?
Your AI mental health chatbot gave harmful advice to a user in crisis. How do you mitigate harm?
Your AI system caused incorrect critical decisions. How do you run a blameless post-mortem?
Radiologists agree with AI 98% of the time, even when it is wrong. How do you prevent human over-reliance on AI?
Your content moderation flags normal cultural expressions as offensive in other markets. How do you adapt cross-culturally?
Your AI training produces massive carbon emissions. How do you reduce environmental impact?
Multimodal AI
What are Multimodal AI models, and how do they process different types of data?
Answer: Multimodal AI
How do vision-language models process images?
How does CLIP work, and why is it important for multi-modal AI?
What are the key architectures for multi-modal models?
How does image generation work with diffusion models (Stable Diffusion, DALL-E, Flux)?
Answer: Diffusion Models
What is text-to-speech (TTS), and what models are used for it?
How does speech-to-text (Whisper) work?
What is multi-modal RAG, and how does it differ from text-only RAG?
How do you build a system that processes both images and text?
What are multi-modal embeddings, and how are they used for cross-modal search?
How do you evaluate multi-modal AI systems?
What are the challenges of real-time multi-modal AI processing?
How do you handle video understanding with AI?
What is visual question answering (VQA)?
What is document understanding, and how do models parse documents with layouts?
How do you fine-tune a vision-language model?
What are the latency and cost considerations for multi-modal AI in production?
How do you handle multi-modal content moderation?
What is text-to-video generation, and what are the current state-of-the-art approaches?
Explain Multimodal Fusion Techniques: Early Fusion vs Late Fusion.
Your vision-language model generates factually incorrect image descriptions. How do you fix it?
Your VLM answers single-image questions but fails on multi-page documents. How do you fix it?
Your multimodal LLM ignores the image and generates descriptions from text alone. How do you fix it?
Your diffusion model ignores precise control requirements in text prompts. How do you improve controllability?
Your diffusion model generates sharp but repetitive images. How do you balance quality vs diversity?
Your diffusion model takes too long per image. How do you speed up sampling?
AI Infrastructure and Scalability
How do you improve inference speed in production LLM deployments?
Answer: LLM Inference Optimization
LLM optimization techniques
Answer: LLM optimization techniques
How do you select GPUs for LLM inference?
What is model parallelism vs data parallelism in distributed training?
What is tensor parallelism, and how does it help serve large models?
What is pipeline parallelism?
How does continuous batching improve LLM inference throughput?
Answer: Continuous Batching in LLMs
What is speculative decoding, and how does it speed up inference?
Answer: Speculative Decoding
What is KV cache, and how do you manage memory for it?
Answer: What is KV Cache in LLMs?
What is Paged Attention?
Answer: Paged Attention in LLMs
How does GGUF work?
Answer: How does GGUF work?
How do you optimize inference for edge and mobile deployment?
What is model quantization (INT8, INT4, FP16, BF16), and how does it affect quality?
Answer: Explained in this video: AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization
How do you implement auto-scaling for AI workloads?
What is the role of load balancing in AI serving infrastructure?
How do you manage GPU memory for serving multiple models?
What is model sharding, and when would you use it?
How do you implement request queuing and priority scheduling for AI services?
What are the cost trade-offs between self-hosted and API-based AI inference?
How do you handle cold start latency for serverless AI deployments?
How do you implement model caching to reduce redundant computations?
What is the difference between synchronous and asynchronous inference, and when do you use each?
What is FSDP (Fully Sharded Data Parallel), and how does it differ from DeepSpeed ZeRO?
How do you monitor and profile LLM inference in production (TTFT, inter-token latency, GPU utilization)?
What is model routing at the infrastructure level, and how do you route requests based on complexity and cost?
Answer: LLM Routing
Coding and Practical Implementation
Implement a basic RAG pipeline using an embedding model and a vector database.
Build a simple AI agent with tool use (e.g., calculator, web search).
Implement semantic search using embeddings and cosine similarity.
Write code for different text chunking strategies (fixed-size, recursive, semantic).
Implement a prompt template system with variable substitution.
Build an evaluation pipeline for LLM outputs using LLM-as-a-judge.
Implement streaming responses for an LLM API.
Answer: How does Token Streaming work?
Build a simple vector similarity search from scratch.
Implement a conversation memory system for a chatbot (sliding window, summary, buffer).
Write code to detect and handle hallucinations in LLM outputs.
Implement a retry mechanism with exponential backoff for LLM API calls.
Write a function calling (tool use) handler for an LLM API.
Implement a simple re-ranker for search results.
Build a basic document parser that extracts text from PDFs and splits it into chunks.
Implement cosine similarity, dot product, and Euclidean distance functions from scratch.
Write code to implement token counting and context window management.
Build a simple prompt versioning system.
Implement a caching layer for LLM responses.
Implement semantic caching for LLM queries (cache responses for semantically similar queries).
Write code to detect prompt injection attempts in user inputs.
Implement an LLM output guardrails system that checks for off-topic responses and PII leakage.
Build a multi-agent system where agents have different roles and collaborate on a task.
Answer: Multi-Agent Systems
Behavioral and Scenario-Based Questions
What is AI Engineering, and how does it differ from Machine Learning Engineering?
How do you decide whether a problem needs AI or a traditional software solution?
How do you measure the ROI of an AI feature?
How do you handle hallucinations when they occur in a production AI system?
How do you decide between using an LLM API vs self-hosting an open-source model?
How do you manage stakeholder expectations for AI projects?
Describe your approach to debugging a poor-performing RAG system.
How do you stay current with the rapidly evolving AI landscape?
How do you balance innovation with reliability in AI systems?
Tell me about a challenging AI project you worked on. What was the problem? What approach did you take? What trade-offs did you make? What was the outcome?
How would you handle a situation where an AI model produces biased or harmful outputs in production?
How do you approach cost optimization for an AI system that's exceeding budget?
Describe a time when you had to choose between model accuracy and latency. How did you make the decision?
How would you handle a situation where your AI system's quality degrades over time?
How do you communicate AI limitations to non-technical stakeholders?
How would you approach building an AI feature with limited labeled data?
Describe your experience working with cross-functional teams on AI projects.
Where do you see AI engineering heading in the next 3-5 years?
Why are you interested in this AI engineering role?
Your PM wants to ship an AI feature with a 15% hallucination rate on edge cases. How do you communicate the risk?
A non-technical executive asks why your AI feature cannot be 100% accurate. How do you explain LLM limitations?
You need to choose between a complex agentic system that scores 15% better on benchmarks, or a simpler RAG pipeline that is easier to maintain. How do you decide?

LangChain
Why was LCEL (LangChain Expression Language) introduced, and what are its benefits?
Explain the core components of the Runnable interface: Passthrough, Parallel, Lambda, and Sequence.
Why is LangChain deprecating legacy chains like LLMChain or RetrievalQA?
How does conversational memory work in modern LangChain?
How do you stream tokens and intermediate steps in LangChain?
How do you implement tool calling and ensure structured outputs in LangChain?
How does the LangChain callback system work, and how does it relate to LangSmith?
What are the best practices for document chunking and retrieval using LangChain?
How do you create custom tools in LangChain with validation?
How does vector store abstraction work in LangChain, and how do you configure custom retrievers?

LangGraph
What is LangGraph, and when would you use it over standard LangChain agents?
How does state management and "reducers" work in LangGraph?
Explain Nodes, Edges, and Conditional Edges in LangGraph.
How does LangGraph support memory persistence and checkpointing?
How do you implement Human-in-the-Loop (Interrupts) in LangGraph?
What is "Time Travel" and "State Replay" in LangGraph, and how does it help debugging?
How do you handle parallel node execution and fan-out/fan-in in LangGraph?
How does streaming work in LangGraph, and what is the difference between "values" and "updates" streaming?
How do you implement modularity using Subgraphs in LangGraph?
How do you prevent infinite loops in cyclical LangGraph agents?

Python

1. What are the differences between List, Tuple, Set, and Dictionary?
Answer: 
- **List**: Ordered, mutable, allows duplicate elements. E.g., `[1, 2, 2]`
- **Tuple**: Ordered, immutable, allows duplicate elements. E.g., `(1, 2, 2)`
- **Set**: Unordered, mutable, unique elements only. E.g., `{1, 2}`
- **Dictionary**: Key-value pairs, unique/hashable keys, ordered by insertion. E.g., `{'a': 1}`

2. Why are tuples immutable?
Answer: Protecting data integrity, ensuring hashability (so they can be dictionary keys or set elements), and optimizing performance (faster instantiation and less memory overhead).

3. What is Python's GIL (Global Interpreter Lock)?
Answer: A mutex in CPython that ensures only one thread executes Python bytecode at a time, preventing multi-threaded CPU-bound concurrency but releasing the lock for I/O operations.

4. How does Python manage memory?
Answer: Through a private heap with automatic memory management using reference counting for immediate cleanup and a generational garbage collector to resolve reference cycles.

5. What is reference counting?
Answer: A memory management mechanism where Python tracks the number of references to each object. When an object's reference count drops to 0, its memory is immediately deallocated.

6. What is garbage collection?
Answer: Python's background generational memory manager that detects and sweeps cyclical references (objects referencing each other but unreachable from the code), which reference counting alone cannot clean.

7. Difference between == and is?
Answer: `==` compares the equality of values (do they have the same data?), whereas `is` compares object identity (do they point to the exact same memory address/ID?).

8. What are mutable and immutable objects?
Answer: Mutable objects can be modified after creation (e.g., lists, dicts, sets). Immutable objects cannot be changed (e.g., ints, strings, tuples).

9. What happens internally when you execute:
a = [1,2,3]
b = a
Answer: Python creates a list object `[1, 2, 3]` in memory and binds name `a` to it (ref count = 1). The statement `b = a` binds the name `b` to the *same* list object, incrementing its ref count to 2 without copying the list.

10. Deep Copy vs Shallow Copy
Answer: A shallow copy (`copy.copy()`) creates a new outer object but references the original inner/nested objects. A deep copy (`copy.deepcopy()`) recursively copies all nested objects, creating completely independent copies.

OOP Questions

11. What are the four pillars of OOP?
Answer: 
- **Encapsulation**: Grouping data and methods while restricting direct access.
- **Abstraction**: Hiding complex implementation details, exposing only essential interfaces.
- **Inheritance**: Allowing a child class to inherit attributes and methods from a parent class.
- **Polymorphism**: The ability of different classes to respond to the same method signature in their own way.

12. Difference between Abstraction and Encapsulation?
Answer: Abstraction focuses on hiding *complexity* (exposing "what" it does), while encapsulation focuses on hiding *data/details* (restricting "how" variables are accessed).

13. Difference between Method Overloading and Overriding?
Answer: Overloading (not natively supported in Python) defines methods with the same name but different signatures in the same class. Overriding redefines a parent class's method in a child class with the exact same signature.

14. What is Multiple Inheritance?
Answer: A feature where a class inherits attributes and methods from more than one parent class (e.g., `class D(B, C)`).

15. What is MRO (Method Resolution Order)?
class A:
class B(A):
class C(A):
class D(B,C):
Answer: MRO is the order Python uses to search for a method or attribute in a class hierarchy, calculated using the C3 Linearization algorithm. For `class D(B, C)`, the MRO is: `D -> B -> C -> A -> object`.

16. What is a Class Method?
Answer: A method decorated with `@classmethod` that receives the class `cls` as its first argument rather than the instance `self`. It can access and modify class state.

17. What is a Static Method?
Answer: A method decorated with `@staticmethod` that doesn't receive `self` or `cls` as arguments. It behaves like a normal utility function namespace-bound to the class.

18. What is Self?
Answer: An argument representing the specific instance of the class being created or modified, allowing access to its attributes and methods.

19. What is Super()?
Answer: A built-in function that returns a proxy object delegation to parent or sibling classes in the Method Resolution Order (MRO), allowing cooperative multiple inheritance.

20. What are Magic/Dunder Methods?
Answer: Special class methods prefixed and suffixed with double underscores (e.g., `__init__`, `__str__`) that hook into Python's built-in behaviors, operators, and protocols.

Functions

21. What are *args and **kwargs?
Answer: `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

22. What are Lambda Functions?
Answer: Small, anonymous, single-expression functions declared using the `lambda` keyword (e.g., `lambda x, y: x + y`) that implicitly return the evaluated expression.

23. What are Closures?
Answer: Nested functions that retain access to the variables of their enclosing outer function scope even after the outer function has finished executing.

24. What are Decorators?
Answer: Functions that take another function as input, modify/extend its behavior, and return a new function without directly modifying the source code.

Very Important

@login_required
def dashboard():
25. How do decorators work internally?
Answer: They act as syntactic sugar. Writing `@decorator` above a function definition is equivalent to writing `dashboard = decorator(dashboard)`, wrapping the original callable in a new function wrapper.

Iterators & Generators

26. What is an Iterator?
Answer: An object representing a stream of data that implements the `__iter__()` method and `__next__()` method, raising `StopIteration` when elements are exhausted.

27. What is Iteration Protocol?
Answer: A protocol where passing an iterable to `iter()` returns an iterator, and calling `next()` on that iterator yields consecutive items until `StopIteration` is raised.

28. What is a Generator?
yield
Answer: A special iterator created via a function containing the `yield` keyword. It yields values lazily, pausing execution state (variables, instruction pointer) between calls.

29. Why use Generators?
Answer: Memory efficiency. They yield elements one at a time on demand rather than loading an entire dataset/list into memory.

30. Generator vs Normal Function
Answer: A normal function runs to completion and returns a value via `return`, destroying its local state. A generator yields values via `yield`, pausing execution and preserving its state for subsequent calls.

Concurrency

31. Multithreading vs Multiprocessing
Answer: Multithreading runs multiple threads in a single process, sharing memory but restricted by the GIL (only one thread executes Python code at a time). Multiprocessing runs separate processes with separate memory spaces and interpreters, achieving true CPU-bound parallelism.

32. When to use Threading?
Answer: For I/O-bound tasks (e.g., calling web APIs, database queries, reading/writing files) where threads spend most of their time waiting.

33. When to use Multiprocessing?
Answer: For CPU-bound tasks (e.g., heavy math computations, data parsing, machine learning inference) that require continuous CPU cycles.

34. What is Async Programming?
Answer: A cooperative multitasking model where a single thread (using an event loop) schedules and executes asynchronous tasks. Tasks cooperatively yield control via `await` when waiting on I/O.

35. Async vs Multithreading
Answer: Async is single-threaded, cooperative (explicit context switches via `await`), and extremely lightweight. Multithreading is multi-threaded, preemptive (OS-managed context switches), and prone to race conditions.

36. What is asyncio?
Answer: Python's built-in library for writing concurrent code using the `async`/`await` syntax, containing APIs for running event loops and handling asynchronous tasks.

37. Event Loop Explain
Answer: The engine of async execution. It monitors I/O events, runs a queue of active coroutines/tasks, and handles context switches when tasks await resources.

38. What are Coroutines?
Answer: Functions declared with `async def`. When called, they return a coroutine object rather than executing immediately, needing to be awaited or run on the event loop.

39. What happens when await is called?
Answer: The execution of the current coroutine is suspended, and control is returned to the event loop, allowing other tasks to run until the awaited operation completes.

40. Why is async important for AI applications?
Answer: AI systems heavily depend on I/O-bound operations: making concurrent LLM API calls, querying vector databases, retrieving document chunks, and streaming tokens to clients. Async handles these tasks efficiently without blocking the system.

Exception Handling

41. try-except-finally flow?
Answer: 
- `try`: Code that might raise an exception.
- `except`: Catches and handles exceptions.
- `else`: Runs only if no exceptions were raised.
- `finally`: Runs under all circumstances (used for cleanup).

42. Difference between Exception and Error?
Answer: In Python, `Exception` (inheriting from `BaseException`) represents disruptions that can be caught and recovered from. Errors (like `SyntaxError` or `SystemError`) represent critical issues that usually cannot or should not be caught.

43. How to create Custom Exceptions?
Answer: By defining a class that inherits from the built-in `Exception` class: `class CustomError(Exception): pass`.

44. What happens if exception isn't handled?
Answer: The exception propagates up the call stack. If it reaches the main program entry without being caught, Python prints a traceback and crashes.

Advanced Python

45. What is Monkey Patching?
Answer: The dynamic modification of classes or modules at runtime (e.g., swapping a production function with a mock during testing).

46. What is Duck Typing?
Answer: A design style where an object's suitability is determined by the presence of certain methods/properties rather than its explicit class inheritance ("if it walks and quacks like a duck, it's a duck").

47. What are Metaclasses?
Answer: The class of a class. While a class defines instance behavior, a metaclass defines class behavior (e.g., intercepting class creation). The default metaclass is `type`.

48. What is new vs init?
Answer: `__new__` is a static method that *creates* and returns a new instance of the class (runs first). `__init__` is an instance method that *initializes* that instance (runs second).

49. What is Context Manager?
with open()
Answer: An object that implements `__enter__` and `__exit__` to setup and teardown resources automatically. It is invoked using the `with` statement.

50. What is Python Packaging?
pip
setuptools
wheel
Answer: The ecosystem of preparing and distributing Python code. `setuptools` compiles and packages the code, `wheel` is the standard built-package binary format, and `pip` installs these packages from registries like PyPI.

Python Coding Questions Frequently Asked in L2

Strings

1. Reverse a String
Input: "hello"
Output: "olleh"
Answer: 
```python
def reverse_string(s: str) -> str:
    return s[::-1]
```

2. Check Palindrome
Input: "madam"
Output: True
Answer: 
```python
def is_palindrome(s: str) -> bool:
    clean_s = "".join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]
```

3. Find First Non-Repeating Character
Input: "aabbccdef"
Output: d
Answer: 
```python
def first_uniq_char(s: str) -> str:
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return ""
```

4. Count Character Frequency
Input: "banana"
Output:
b:1
a:3
n:2
Answer: 
```python
def char_frequency(s: str) -> dict:
    from collections import Counter
    return dict(Counter(s))
```

5. Check Anagram
Input: "listen", "silent"
Output: True
Answer: 
```python
def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)
```

6. Remove Duplicate Characters
Input: "programming"
Output: "progamin"
Answer: 
```python
def remove_duplicate_chars(s: str) -> str:
    return "".join(dict.fromkeys(s))
```

7. Find Most Frequent Character
Input: "banana"
Output: a
Answer: 
```python
def most_frequent_char(s: str) -> str:
    from collections import Counter
    return Counter(s).most_common(1)[0][0]
```

8. Count Vowels and Consonants
Input: "hello world"
Answer: 
```python
def count_vowels_consonants(s: str) -> dict:
    vowels = "aeiou"
    clean_s = [c for c in s.lower() if c.isalpha()]
    v_count = sum(1 for c in clean_s if c in vowels)
    c_count = len(clean_s) - v_count
    return {"vowels": v_count, "consonants": c_count}
```

Lists

9. Remove Duplicates from List
Input: [1,2,2,3,4,4,5]
Output: [1,2,3,4,5]
Answer: 
```python
def remove_duplicates_list(lst: list) -> list:
    return list(dict.fromkeys(lst))
```

10. Find Second Largest Number
Input: [10,20,30,40,50]
Output: 40
Answer: 
```python
def second_largest(lst: list) -> int:
    unique_sorted = sorted(list(set(lst)))
    return unique_sorted[-2] if len(unique_sorted) >= 2 else None
```

11. Find Missing Number
Input: [1,2,3,5]
Output: 4
Answer: 
```python
def find_missing_number(lst: list) -> int:
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(lst)
```

12. Find Duplicate Elements
Input: [1,2,2,3,4,4,5]
Output: [2,4]
Answer: 
```python
def get_duplicates(lst: list) -> list:
    seen, duplicates = set(), set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return list(duplicates)
```

13. Flatten Nested List
Input: [[1,2],[3,4],[5,6]]
Output: [1,2,3,4,5,6]
Answer: 
```python
def flatten(nested: list) -> list:
    return [item for sublist in nested for item in sublist]
```

14. Find Common Elements
Input: a = [1,2,3,4], b = [3,4,5,6]
Output: [3,4]
Answer: 
```python
def common_elements(a: list, b: list) -> list:
    return list(set(a) & set(b))
```

15. Rotate List by K Positions
Input: [1,2,3,4,5], k=2
Output: [4,5,1,2,3]
Answer: 
```python
def rotate_list(lst: list, k: int) -> list:
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
```

Dictionary

16. Word Frequency Counter
Input: "apple banana apple mango banana apple"
Output: {'apple':3, 'banana':2, 'mango':1}
Answer: 
```python
def word_frequency(s: str) -> dict:
    from collections import Counter
    return dict(Counter(s.split()))
```

17. Merge Two Dictionaries
Input: d1 = {"a":1}, d2 = {"b":2}
Answer: 
```python
def merge_dicts(d1: dict, d2: dict) -> dict:
    return d1 | d2
```

18. Sort Dictionary by Value
Input: {"a":3, "b":1, "c":2}
Answer: 
```python
def sort_dict_by_value(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))
```

Numbers

19. Fibonacci Series
Input: 0 1 1 2 3 5 8 (first 7 numbers)
Answer: 
```python
def fibonacci_series(n: int) -> list:
    if n <= 0: return []
    elif n == 1: return [0]
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series
```

20. Check Prime Number
Input: 17
Output: Prime
Answer: 
```python
def is_prime(n: int) -> str:
    if n <= 1: return "Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
```

21. Generate Prime Numbers till N
Input: N=100
Answer: 
```python
def primes_till_n(n: int) -> list:
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes
```

22. Factorial
Input: 5! = 120
Answer: 
```python
def factorial(n: int) -> int:
    if n <= 1: return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

23. Armstrong Number
Input: 153
Answer: 
```python
def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
```

24. Find GCD
Input: 24, 36
Output: 12
Answer: 
```python
def find_gcd(a: int, b: int) -> int:
    import math
    return math.gcd(a, b)
```

Pattern / Logic

25. FizzBuzz
Input: 1 to 100
Answer: 
```python
def fizz_buzz():
    res = []
    for i in range(1, 101):
        if i % 15 == 0: res.append("FizzBuzz")
        elif i % 3 == 0: res.append("Fizz")
        elif i % 5 == 0: res.append("Buzz")
        else: res.append(str(i))
    return res
```

26. Find Longest Word
Input: "I love artificial intelligence"
Output: intelligence
Answer: 
```python
def longest_word(sentence: str) -> str:
    return max(sentence.split(), key=len)
```

27. Find Longest Substring Without Repeating Characters
Input: abcabcbb
Output: 3
Answer: 
```python
def longest_uniq_substring(s: str) -> int:
    char_map = {}
    max_len = start = 0
    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len
```

Python Specific

28. Implement a Decorator
Input:
```python
@timer
def test():
    pass
```
Measure execution time.
Answer: 
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper
```

29. Create a Generator
Input: Generate numbers from 1 to N using yield
Answer: 
```python
def number_generator(n: int):
    for i in range(1, n + 1):
        yield i
```

30. Implement LRU Cache
Input: Cache of size 3, checking evictions
Answer: 
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```


FastAPI

### Basics

1. What is FastAPI?
Answer: A modern, high-performance web framework for building APIs with Python 3.8+ based on standard Python type hints. Built on top of Starlette (for web parts) and Pydantic (for data validation).

2. Why FastAPI over Flask?
Answer: FastAPI provides native asynchronous (`async`/`await`) support, automatic data validation/serialization using Pydantic, and automatic interactive Swagger/ReDoc documentation generation, whereas Flask is synchronous by default and requires separate extensions for these features.

3. Why FastAPI over Django?
Answer: FastAPI is lightweight, async-first, and highly optimized for building microservices and REST/GraphQL APIs. Django is a heavyweight, synchronous full-stack framework with built-in admin panels and ORM, which has more overhead.

4. FastAPI Architecture?
Answer: FastAPI is an ASGI-compatible application layer built on **Starlette** (ASGI toolkit handling routing, sessions, WebSockets) and **Pydantic** (data validation/parsing layer). It uses **Uvicorn** as the underlying ASGI web server.

5. ASGI vs WSGI
Answer:
* **WSGI** (Web Server Gateway Interface): Synchronous protocol. It handles one request per thread/process at a time, making it bad for long-lived connections (WebSockets, streaming).
* **ASGI** (Asynchronous Server Gateway Interface): Successor to WSGI. It supports asynchronous execution, enabling a single process to handle WebSockets, SSE, HTTP streaming, and concurrent long-polling requests.

### API Development

6. How do you create an endpoint?
Answer:
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}
```

7. GET vs POST vs PUT vs PATCH vs DELETE
Answer:
* `GET`: Retrieves data.
* `POST`: Submits data to create a new resource.
* `PUT`: Replaces an entire existing resource.
* `PATCH`: Partially updates an existing resource.
* `DELETE`: Deletes a resource.

8. Path Parameters
Answer: Variable parts of the URL path used to identify a resource.
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

9. Query Parameters
Answer: Key-value pairs added after the `?` in a URL, usually optional and used for filtering/paging.
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

10. Request Body
Answer: The payload sent in the HTTP request (typically JSON), defined using a Pydantic model.
```python
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
@app.post("/items/")
def create_item(item: Item):
    return item
```

### Pydantic

11. What is Pydantic?
Answer: A data validation and settings management library using Python type annotations. It enforces type hints at runtime and provides user-friendly errors when data is invalid.

12. Why does FastAPI use Pydantic?
Answer: To perform automatic request body parsing, runtime data validation, data sanitization/coercion, and response serialization.

13. Data Validation Example
Answer:
```python
from pydantic import BaseModel, EmailStr
class User(BaseModel):
    username: str
    email: EmailStr
    age: int
```

14. Optional Fields
Answer: Defined using `Optional` from the `typing` module or `None` default values (or `str | None` in Python 3.10+).
```python
from typing import Optional
class User(BaseModel):
    bio: Optional[str] = None
```

15. Nested Models
Answer: Pydantic models can contain lists or dicts of other Pydantic models.
```python
class Image(BaseModel):
    url: str
class Item(BaseModel):
    name: str
    images: list[Image]
```

16. Field Validators
Answer: Custom validation logic applied to specific fields using the `@validator` decorator (or `@field_validator` in Pydantic v2).
```python
from pydantic import BaseModel, validator
class User(BaseModel):
    age: int
    @validator("age")
    def must_be_adult(cls, v):
        if v < 18: raise ValueError("Must be 18+")
        return v
```

17. Custom Validation
Answer: Implemented using `@validator` (specific fields) or `@root_validator` (model-wide fields check, like password confirmation matching).

18. Serialization
Answer: The process of converting Pydantic objects or database models back into standard JSON formats. In Pydantic, this is done via `model.dict()` (v1) or `model.model_dump()` (v2).

19. Response Models
Answer: Defining the exact Pydantic model format that the endpoint is allowed to return.
```python
@app.get("/users/{id}", response_model=UserOut)
def read_user(id: int):
    return db_user
```

20. Why Response Models?
Answer: It filters out private/unwanted fields (like hashed passwords), validates outgoing data, format-coerces fields, and automatically documents the response in Swagger.

### Dependency Injection

21. What is Depends()?
Answer: A utility function in FastAPI used to declare a dependency. FastAPI will automatically evaluate the dependency function and inject its return value into the route handler.

22. Why Dependency Injection?
Answer: It maximizes code reuse (e.g. sharing database session creation, JWT verification, query parameters parsing) and makes unit testing easier by allowing dependencies to be easily mocked.

23. Database Dependency Example
Answer:
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

24. Shared Dependencies
Answer: Dependencies that are declared globally or at the router level so that they apply to all endpoints (e.g. enforcing authentication on an entire set of routes).

25. Dependency Lifecycle
Answer: A dependency runs when a request hits the endpoint. If it uses `yield` (like the DB session), it executes the setup code, yields the value to the endpoint, and executes the cleanup code (after `yield`) after the response is sent.

### Async Programming

26. Difference between async def and def
Answer:
* `async def`: Defines a coroutine that runs on the main event loop. It must yield execution via `await` when performing I/O.
* `def`: Defines a synchronous blocking function. FastAPI executes `def` functions on a background thread pool to prevent them from blocking the main event loop.

27. When should async be used?
Answer: For I/O-bound tasks (network requests, calling database queries, sending messages to queues, reading/writing files) where the system spends time waiting.

28. What happens internally in async endpoint?
Answer: When the async endpoint hits an `await` statement, it pauses execution and yields control back to the event loop. The event loop then runs other tasks until the awaited operation signals that it is complete.

29. What is await?
Answer: A keyword that pauses execution of the current coroutine, returning control to the event loop until the awaited task completes and returns its result.

30. Event Loop Explain
Answer: The core engine of async Python. It runs in a loop, scheduling tasks, checking if registered I/O events (like network packets arriving) are ready, and executing active coroutines.

31. Async Database Calls
Answer: Using database drivers that support async (like `asyncpg` or `aiomysql` with `SQLAlchemy`'s `ext.asyncio` extensions) to execute database queries without blocking the event loop.

32. Async HTTP Calls
Answer: Using non-blocking HTTP clients like `httpx` or `aiohttp` to call third-party APIs (like LLM providers) without stopping other requests.
```python
import httpx
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.openai.com/...")
```

33. Blocking vs Non-Blocking
Answer:
* **Blocking**: A synchronous execution model where the thread is held and cannot perform any other work while waiting for an operation to finish.
* **Non-Blocking**: An asynchronous execution model where the thread is released to perform other tasks while waiting for the operation to complete.

34. Why async matters in GenAI APIs?
Answer: AI APIs are highly I/O-bound: calls to LLM providers (which can take seconds to generate text) or document retrieval from vector databases can block the system. Async allows the server to handle thousands of simultaneous client connections and stream tokens concurrently.

35. Async vs Threading
Answer:
* **Async**: Single-threaded, cooperative multitasking. The developer decides when to switch contexts (via `await`). Low overhead, supports high concurrency.
* **Threading**: Multi-threaded, preemptive multitasking managed by the OS. Context switches are arbitrary, meaning there is thread overhead and potential for race conditions.

### Authentication

36. JWT Authentication
Answer: JSON Web Token authentication. Users log in with credentials, the server generates a signed cryptographical token (JWT), and the client sends this token in the header (`Authorization: Bearer <token>`) for subsequent requests.

37. OAuth2 Flow
Answer: The industry standard protocol for authorization. FastAPI integrates with the **Authorization Code Flow with PKCE** or **Resource Owner Password Credentials Flow** to safely authenticate clients and issue access tokens.

38. Refresh Tokens
Answer: Long-lived tokens stored securely on the client side, used to request new short-lived access tokens from the auth server once they expire without prompting user re-login.

39. Access Tokens
Answer: Short-lived cryptographic tokens (usually JWTs, valid for 15-30 minutes) used by the client to authorize API requests.

40. How FastAPI handles security?
Answer: FastAPI provides the `fastapi.security` module which offers built-in classes (`OAuth2PasswordBearer`, `APIKeyHeader`, `HTTPBasic`) that extract credentials from headers/cookies and integrate directly into the dependency injection engine.

### Database

41. FastAPI with SQLAlchemy
Answer: Implemented by declaring a database engine, creating a `sessionmaker`, and using a dependency function (`get_db`) to yield session instances into endpoints.

42. ORM vs Raw SQL
Answer:
* **ORM** (Object-Relational Mapper): Maps database tables to Python classes. Safer (prevents SQL Injection), faster to write, but can add query overhead.
* **Raw SQL**: Hand-written queries. Highly optimized, but tedious to write and maintain, and requires careful parameters parsing to prevent security risks.

43. Session Management
Answer: Creating a database session per request and ensuring it is closed (`db.close()`) once the request completes, which is managed cleanly using a yielding FastAPI dependency.

44. Connection Pooling
Answer: A cache of active database connections maintained by the server. Instead of creating and destroying connections for every request (which is slow), FastAPI/SQLAlchemy reuse connections from the pool.

45. Async SQLAlchemy
Answer: Using `create_async_engine` and `AsyncSession` alongside an async driver (like `asyncpg`) to perform database queries in a non-blocking manner.

### Production Deployment

46. How do you deploy FastAPI?
Answer: FastAPI applications are deployed inside Docker containers using an ASGI stack.
```
Client
  ↓
Nginx
  ↓
Gunicorn
  ↓
Uvicorn Workers
  ↓
FastAPI
```
Explanation: Nginx acts as the reverse proxy (handling SSL/static content), Gunicorn acts as the process manager, which spawns and runs Uvicorn workers (`UvicornWorker`) to execute the FastAPI application.

47. What is Uvicorn?
Answer: A lightning-fast ASGI web server implementation for Python, built on `uvloop` (a fast C implementation of the event loop) and `httptools`.

48. What is Gunicorn?
Answer: A WSGI HTTP server commonly used as a process manager in production to monitor, spawn, restart, and scale worker processes (like Uvicorn workers) to ensure high availability.

49. How to Dockerize FastAPI?
Answer:
```dockerfile
FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:80"]
```

50. How to scale FastAPI for 10,000 concurrent users?
Answer:
1. Set up horizontal scaling behind a Load Balancer (e.g. AWS ALB or Kubernetes Ingress).
2. Run FastAPI asynchronously using Uvicorn workers.
3. Implement Connection Pooling and Async database drivers to prevent database bottlenecks.
4. Use **Redis** for session management, semantic caching, and rate limiting.
5. Offload heavy computation (like document processing or LLM inference) to Celery task queues.

### FastAPI + GenAI Questions

51. How would you expose an LLM through FastAPI?
Answer: Expose a POST endpoint that accepts parameters (prompt, temperature, etc.) via a Pydantic model, invokes the LLM client (e.g. OpenAI or Anthropic SDKs), and returns the generated text.
```python
@app.post("/generate")
async def generate_text(payload: PromptPayload):
    response = await openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": payload.prompt}]
    )
    return {"response": response.choices[0].message.content}
```

52. How would you stream LLM responses?
Answer: By using `StreamingResponse` from `fastapi.responses` combined with an asynchronous generator function that streams chunks from the LLM provider.
```python
from fastapi.responses import StreamingResponse

async def token_generator(prompt):
    stream = await openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    async for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content

@app.get("/stream")
async def stream_endpoint(prompt: str):
    return StreamingResponse(token_generator(prompt), media_type="text/event-stream")
```

53. How would you upload PDFs for RAG?
Answer: Define a POST endpoint that accepts files via `UploadFile`, saves/reads the file stream, parses it using a PDF extractor, splits it into chunks, generates embeddings, and saves them to the vector store.
```python
from fastapi import UploadFile, File
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    # Parse PDF contents, chunk, embed, and store in FAISS/Pinecone
    return {"filename": file.filename, "status": "indexed"}
```

54. How would you process large documents asynchronously?
Answer: By offloading the document processing to a background task using FastAPI's `BackgroundTasks` or a dedicated distributed task queue like **Celery** with Redis, preventing the HTTP request from timing out.
```python
from fastapi import BackgroundTasks

def process_pdf_task(file_path):
    # Heavy parsing, embedding, and indexing work
    pass

@app.post("/process-large-doc")
async def process_doc(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_pdf_task, "path/to/doc.pdf")
    return {"message": "Document processing started in background"}
```

55. How would you integrate LangChain with FastAPI?
Answer: By instantiating LangChain chains, runnables, or agents globally or inside dependency injection, and invoking them inside endpoints. For streaming, you can use LangChain's async streaming API (`astream` or `astream_events`) wrapped in a FastAPI `StreamingResponse`.

56. How would you handle 1000 simultaneous AI requests?
Answer:
1. Use fully asynchronous routing to avoid blocking thread pools.
2. Implement **Prompt Caching** (supported by Anthropic/OpenAI) to reduce latency and processing overhead.
3. Deploy FastAPI behind a load balancer on multiple containers.
4. Use a Redis-based rate limiter to protect endpoints from overload.
5. Implement request queuing/buffering.

57. How would you cache LLM responses?
Answer: By storing prompt/response pairs in a caching layer. For exact match lookup, use standard key-value caching. For semantic similarity match lookup (handling slightly rephrased queries), implement **Semantic Caching** using vector similarity search.

58. Redis vs Memory Cache?
Answer:
* **Memory Cache**: Extremely fast, but local to a single container/process. It gets cleared on container restart and cannot be shared across multiple scaled instances.
* **Redis**: Distributed and persistent. It can be shared across all scaled instances of FastAPI, makes capacity planning easier, and supports semantic vector indices.

59. How would you implement conversation history?
Answer: By storing conversation history (list of user/assistant messages) in **Redis** indexed by a unique `session_id`. When a request comes in, retrieve the history, append the new message, send it to the LLM, and update the store.
```python
@app.post("/chat")
async def chat(session_id: str, message: str):
    history = await redis.get(session_id) or []
    history.append({"role": "user", "content": message})
    response = await call_llm(history)
    history.append({"role": "assistant", "content": response})
    await redis.set(session_id, history)
    return {"response": response}
```

60. How would you secure an AI API from prompt injection?
Answer:
1. Use structured inputs (JSON schemas) instead of passing raw, unvalidated text blobs.
2. Enforce strict **system prompts** that instruct the model to ignore user attempts to override instructions.
3. Run an validation layer (like **Llama Guard** or **NeMo Guardrails**) to check inputs before sending them to the core LLM.
4. Implement input sanitization and length limits on user prompts.


Resume-Based Questions

### Section 1: General/Introductory Questions

1. Tell me about yourself.
Answer: "I am currently a Senior Software Developer at Yotta Infrastructures with 3+ years of experience building enterprise applications using Angular, Flutter and Python. While working on large-scale monitoring and customer portals, I developed a strong interest in AI engineering. Over the last year I built production-grade AI applications such as Nyaya-Pro, JobPilot AI and ExamGenie AI using FastAPI, LangChain, CrewAI, Gemini and vector databases. I now want to leverage both my software engineering foundation and AI expertise in a dedicated GenAI role."

Follow-ups:
* **Why AI?**: AI is transitioning from research to production engineering. Building systems that can reason, orchestrate, and retrieve information dynamically represents the next paradigm of software development.
* **Why leave frontend?**: I am not abandoning frontend; rather, I'm expanding my capabilities. Frontend taught me clean architecture and performance, but building the backend reasoning engines (AI agents/RAG) is technically more challenging and impactful.
* **Why not continue as full-stack?**: I want to specialize. While I can build end-to-end, specializing in GenAI engineering allows me to deeply understand retrieval orchestration, agent loops, and model optimization.

2. Why are you moving from Angular to AI?
Answer: "Frontend development taught me scalable architecture, performance optimization and production deployments. AI engineering allows me to build intelligent systems that can reason, retrieve information and automate workflows. I find this area more impactful and technically challenging."

Follow-up:
* **Why didn't you become a full-stack developer first?**: I did work across the stack (including Python backend work at Yotta), but the rapid emergence of agentic workflows and RAG convinced me to focus my efforts on AI engineering.
* **How much production AI experience do you actually have?**: I have spent the last year designing, benchmarking, and building AI tools (like Nyaya-Pro and JobPilot AI) utilizing tools like FastAPI, LangChain, and CrewAI, deploying them in sandboxed and staging environments.

3. Why LTIMindtree?
Answer: LTIMindtree has a strong focus on enterprise AI adoption, working with global clients on large-scale AI transformation projects. Joining LTIMindtree gives me the opportunity to build production-grade AI systems, handle real-world retrieval challenges (like hybrid search and multi-agent orchestration), and scale AI solutions for enterprise clients.

4. Why should we hire you over pure AI candidates?
Answer: "Many AI candidates have strong model knowledge but limited production experience. I bring both enterprise software engineering and AI implementation experience. I know how to integrate models into robust, maintainable, and scalable applications."

Follow-up:
* **Give examples**: In Nyaya-Pro, I didn't just call an API; I built an agentic router, implemented custom semantic cross-encoder reranking to optimize retrieval quality, and set up local FAISS indexes to manage costs and latency.

5. What is your biggest achievement?
Answer: My major achievements combine engineering rigor with AI innovation:
* **Angular 14 → 17 Migration**: Upgraded the core dashboard in OneYotta Portal, managing breaking changes and RxJS migrations smoothly.
* **Dashboard Performance**: Improved dashboard response and rendering speeds by 30% via lazy loading and NgRx state management.
* **Nyaya-Pro**: Architected and built an end-to-end legal assistant that indexes complex Indian law codes using a retrieval-reranker pipeline.

### Section 2: Yotta Experience (Questions 6-15)

6. Explain OneYotta Portal.
Answer: OneYotta Portal is the primary customer portal at Yotta Infrastructures, allowing clients to manage cloud resources, check resource monitoring metrics, raise support tickets, and view billing details.

Follow-up:
* **Architecture?**: Built with Angular on the frontend for dynamic rendering and State management (NgRx), communicating via REST APIs with a microservices-based backend.
* **User count?**: Handles thousands of active enterprise B2B customers.
* **Authentication?**: Integrated with Keycloak and Azure AD for secure Single Sign-On (SSO).

7. Explain Keycloak integration.
Answer: I integrated Keycloak as our Identity Provider (IdP) for SSO. It handles authentication and issues tokens to authorize API access.

Follow-up:
* **OAuth flow?**: Used the Authorization Code Flow with Proof Key for Code Exchange (PKCE) for secure frontend authentication.
* **Access Token?**: Short-lived JWT containing user roles used to authenticate API calls.
* **Refresh Token?**: Long-lived token stored securely to fetch a new access token without re-authenticating the user.
* **JWT?**: JSON Web Token consisting of Header, Payload, and Signature, verified by the backend using Keycloak's public keys.

8. What challenges did you face during Angular migration?
Answer: Migrating OneYotta from Angular 14 to 17 involved moving to a standalone component structure, adopting the new control flow syntax, and updating deprecated dependencies.

Follow-up:
* **Breaking changes?**: Node module incompatibilities and changes in class-based lifecycle hooks were resolved by updating code to use inject-based DI and standalone components.
* **RxJS migration?**: Handled changes in operator signatures (like `switchMap` and `combineLatest`), replacing deprecated syntax and cleaning up subscriptions using `takeUntilDestroyed`.

9. How did you improve dashboard performance by 30%?
Answer: Optimized the portal dashboard by adopting:
1. **Lazy Loading**: Splitting the bundles so that components are loaded only when navigated to.
2. **NgRx Optimization**: Reducing redundant selector computations and batching actions.
3. **API Optimization**: Consolidating requests and introducing caching for static/slow-changing metadata.
4. **OnPush Change Detection**: Stopping Angular's default change detection from running on unchanged subtrees.

Follow-up:
* **How did you measure it?**: Measured using Chrome DevTools (Lighthouse, Core Web Vitals) and Angular DevTools, tracking reductions in bundle size and scripting time.

10. Explain CCTV streaming optimization.
Answer: Optimized live playback streams on our security dashboard to reduce latency and CPU usage during simultaneous camera feeds.

Follow-up:
* **Protocol used?**: Transited from RTSP to WebRTC for low-latency streaming.
* **Latency reduction?**: Latency dropped from ~2-3 seconds to sub-500ms.
* **WebRTC?**: Set up a signaling server and STUN/TURN servers to establish peer-to-peer connections between client and streaming gateways.

11. Explain MyPortal architecture.
Answer: An internal application at Yotta used by operations teams to track data center assets, tickets, and facility parameters in real-time.

Follow-up:
* **Backend?**: Built with Python (FastAPI/Django) communicating with PostgreSQL.
* **Real-time updates?**: Used WebSockets to push live facility alerts and ticket updates directly to the operational dashboards.

12. Why NgRx?
Answer: To maintain a single source of truth for global state (user profiles, system configs, permissions) across highly nested and sibling components, avoiding complex prop-drilling.

Follow-up:
* **Redux principles?**: Single source of truth, state is read-only (mutated only by dispatching actions), and changes are made with pure functions (reducers).
* **Store lifecycle?**: Component dispatches an Action -> Effect intercepts for API call -> Reducer updates state -> Store notifies Selectors -> UI updates.

13. How do you handle large datasets in Angular?
Answer: We use virtual scrolling (rendering only visible rows in the viewport), pagination, pagination-at-DB-level, and trackBy functions in `*ngFor` loops to prevent re-rendering entire lists.

14. How do you manage application state?
Answer: For global/complex state we use NgRx. For local/simple component state, we use Angular Services with RxJS BehaviorSubjects or local state signals.

15. Most difficult bug you solved?
Answer: A memory leak in the OneYotta portal where navigations between monitoring tabs caused the tab component's RxJS subscriptions to accumulate. I diagnosed it using Chrome Heap Snapshots and fixed it by implementing `takeUntil` auto-unsubscribe patterns.

### Section 3: Nyaya-Pro (Questions 16-25)

This is where most LTIMindtree interviewers will spend time.

16. Explain Nyaya-Pro architecture.
Answer: Nyaya-Pro is an intelligent legal document assistant that queries Indian law files.
```
User
 ↓
Query Router
 ↓
Retriever
 ↓
FAISS
 ↓
Re-ranker
 ↓
Gemini
 ↓
Answer
```

17. Why legal domain?
Answer: Legal texts are long, dense, and full of cross-references. Lawyers spend hours searching for specific precedents. Nyaya-Pro automates this search, saving time and improving legal research efficiency.

18. What documents did you use?
Answer: Focuses on Indian statutes and legal manuals.

Follow-up:
* **Constitution?**: Indexed the complete Constitution of India.
* **BNS?**: Bharatiya Nyaya Sanhita (criminal code).
* **BNSS?**: Bharatiya Nagarik Suraksha Sanhita (criminal procedure).
* **CPC?**: Code of Civil Procedure.

19. What embedding model did you use?
Answer: Used `bge-large-en-v1.5` from HuggingFace.

Follow-up:
* **Why that model?**: It ranks highly on the MTEB (Massive Text Embedding Benchmark) for retrieval tasks, offers 1024-dimension embeddings, and captures legal semantics extremely well.

20. Why FAISS?
Answer: FAISS (Facebook AI Similarity Search) is an open-source, highly optimized library for dense vector similarity search.

Follow-up:
* **Why not Pinecone?**: For this application, a local, self-hosted index was preferred to keep data within the local infrastructure (data sovereignty for legal documents) and avoid subscription costs.

21. Explain chunking strategy.
Answer: Used semantic chunking backed by recursive text splitting.

Follow-up:
* **Chunk size?**: ~512 tokens.
* **Overlap?**: 50 tokens (to preserve context boundaries between chunks).

22. Explain semantic search.
Answer: Vector search that matches queries to documents based on conceptual meaning rather than keyword matching, converting texts into dense vectors and finding proximity using similarity metrics.

23. What is reranking?
Answer: Reranking takes the top $K$ results retrieved by the bi-encoder (vector DB) and re-evaluates them using a more powerful cross-encoder model to sort them by actual relevance to the query.

Follow-up:
* **Cross-Encoder vs Bi-Encoder**: Bi-encoders embed query and documents separately (fast vector search). Cross-encoders process the query and document together, outputting a direct similarity score (slower but much more accurate).

24. What causes hallucination?
Answer: Hallucination occurs when the LLM generates plausible-sounding but factually incorrect information due to gaps in the prompt context or out-of-domain queries.

Follow-up:
* **How did Nyaya-Pro reduce hallucinations?**: By forcing the model to only answer based on the retrieved context, implementing strict system prompts, and requiring direct section/clause citations.

25. What happens if no relevant document is found?
Answer: The system prompt instructs the model to state: "I cannot find relevant information in the provided legal source documents" rather than generating an answer.

### Section 4: JobPilot AI (Questions 26-32)

26. Explain JobPilot AI architecture.
Answer: JobPilot AI is an automated resume optimizer built with CrewAI.
1. A user uploads a resume and job description.
2. CrewAI assigns tasks to specialized agents.
3. The final outputs (optimized resume bullet points, cover letter) are returned to the user.

27. Why CrewAI?
Answer: CrewAI excels at role-playing agent orchestration where agents require clean sequential or hierarchical pipelines to execute tasks cooperatively.

Follow-up:
* **Why not LangGraph?**: LangGraph is ideal for complex, stateful cycles and flowcharts. CrewAI provided a cleaner out-of-the-box abstraction for simple role-based workflows without excessive custom loop coding.

28. What agents did you create?
Answer:
1. **Resume Analyzer**: Examines current resume structure.
2. **ATS Optimizer**: Identifies keyword gaps based on the job description.
3. **Cover Letter Writer**: Drafts customized cover letters.
4. **Reviewer**: Evaluates the final results against the initial guidelines.

29. How do agents communicate?
Answer: CrewAI manages agent communication through task outputs. The output of one agent's task is passed as context input to the next agent's task, mimicking a pipeline.

30. How do you prevent infinite loops?
Answer: Enforced max iterations limits (`max_iter`) on each agent and set strict timeouts to prevent agents from repeatedly calling tools without reaching a conclusion.

31. Why Groq?
Answer: Groq provides ultra-fast LLM inference using LPU (Language Processing Unit) hardware.

Follow-up:
* **Groq vs OpenAI?**: Groq API is significantly faster (often 200-300+ tokens per second), which is essential for interactive agent loops where latency accumulates.

32. Ollama vs Groq?
Answer: Ollama runs open-source models locally (useful for private developer testing). Groq provides hosted, highly accelerated open-source models (Llama 3, Mixtral) in production with enterprise scalability.

### Section 5: ExamGenie AI (Questions 33-37)

33. Explain ExamGenie architecture.
Answer: ExamGenie AI parses study documents and automatically generates interactive MCQs and study cards. It uses FastAPI for the API layer and Gemini Flash to analyze documents and generate structured JSON outputs.

34. How do you process PDFs?
Answer: Uploaded PDFs are parsed to extract textual content and structure.

Follow-up:
* **Libraries used?**: Used `PyPDF2` / `pdfplumber` for text extraction, and OCR when handling scanned image PDFs.

35. How do you generate MCQs?
Answer: Extracted study text is chunked, and Gemini Flash is prompted to generate dynamic multiple-choice questions, specifying correct answers, distractors, and educational explanations.

36. How do you evaluate answer quality?
Answer: User answers are compared against the correct options. We run LLM evaluation prompts to check partial correctness on open-ended study cards.

37. Why Gemini Flash?
Answer: Gemini Flash is highly cost-effective, supports a massive context window (1 million tokens), and is extremely fast.

Follow-up:
* **Gemini Flash vs GPT-4o?**: Flash is significantly cheaper and faster, making it perfect for processing hundreds of study pages and generating structured questions at scale.

### Section 6: FastAPI (Questions 38-42)

38. Why FastAPI?
Answer: It is extremely fast (performance on par with Go/NodeJS), uses Pydantic for automatic request validation, supports native async, and generates OpenAPI documentation out-of-the-box.

Follow-up:
* **FastAPI vs Flask**: Flask is synchronous and requires third-party plugins for validation and documentation. FastAPI is asynchronous, type-hint driven, and self-documenting.

39. Explain async APIs.
Answer: APIs defined with `async def` that yield control back to the event loop during I/O operations (like database queries or external LLM calls), allowing a single process to handle thousands of concurrent requests.

40. Explain dependency injection.
Answer: Declaring required resources (like db sessions or security credentials) as parameters using `Depends()`. FastAPI resolves and injects them before running the endpoint.

41. How did you deploy FastAPI?
Answer: Deployed using Uvicorn as the ASGI server inside a Docker container.

Follow-up:
* **Docker/Nginx/Gunicorn?**: The Docker container runs Gunicorn with Uvicorn workers (`UvicornWorker`) to manage multiple processes. Nginx is set up as a reverse proxy to handle SSL and static assets.

42. How would you scale FastAPI?
Answer: Run multiple container instances behind a load balancer (using Kubernetes or AWS ECS) and scale Uvicorn worker counts per CPU core.

### Section 7: GenAI Deep Dive (Questions 43-50)

43. What is RAG?
Answer: Retrieval-Augmented Generation. A pattern where relevant external data is retrieved and appended to the LLM's prompt context, allowing the model to answer queries using up-to-date or private documents.

Follow-up:
* **Why not fine-tuning?**: Fine-tuning changes model behavior/style but is expensive, prone to hallucinations, and does not support dynamic document updates or access controls. RAG updates instantly and cites references.

44. Explain embeddings.
Answer: Numerical vector representations of text where semantically similar concepts are located close to each other in a high-dimensional vector space.

Follow-up:
* **How are embeddings generated?**: By passing text through an embedding model (like `text-embedding-3-small` or `bge-large-en`), which outputs an array of floats (vectors).

45. Explain vector databases.
Answer: Specialized databases designed to store and index high-dimensional vectors, enabling extremely fast nearest-neighbor searches (like Cosine Similarity) across millions of entries.

Follow-up:
* **FAISS vs Pinecone**: FAISS is a local, self-hosted library optimized for CPU/GPU vector searches. Pinecone is a fully managed cloud vector database service designed for scale and multi-tenancy.

46. What is cosine similarity?
Answer: A metric measuring the cosine of the angle between two vectors in a multi-dimensional space:
$$\text{Similarity} = \frac{A \cdot B}{\|A\| \|B\|}$$
It outputs a value between -1 and 1, indicating how semantically similar the represented texts are.

47. Explain prompt engineering.
Answer: The practice of designing, structuring, and optimizing prompt instructions (using patterns like Chain of Thought, few-shot, or role prompting) to guide LLMs to produce accurate and consistent outputs.

48. What is an AI Agent?
Answer: An autonomous system powered by an LLM that can make decisions, use tools (like databases or calculators), write plans, and run in loops to achieve a specified goal.

Follow-up:
* **When should you NOT use agents?**: For highly predictable, deterministic tasks where traditional rule-based coding or sequential pipelines are faster, cheaper, and less prone to agent logic loops.

49. Explain LangChain architecture.
Answer: An open-source framework for building applications with LLMs. Key components include Models (LLMs/Embeddings), Prompts, Chains (sequencing operations), Indexes (document loading/vector stores), and Agents (reasoning loops).

Follow-up:
* **Chains vs Agents**: Chains are hard-coded, sequential execution pipelines. Agents use the LLM as a reasoning engine to dynamically decide the sequence of steps and tools to execute.

50. If I give you ₹1 crore and ask you to build ChatGPT for legal documents, what architecture would you design?
Answer: I would design a robust, high-performance retrieval and generation system:
```
Frontend (React/Next.js)
 ↓
FastAPI Gateway
 ↓
LangGraph Orchestration
 ↓
Embedding Model (cohere/bge)
 ↓
Vector DB (Qdrant/Pinecone) + Hybrid BM25 Search
 ↓
Cross-Encoder Reranker
 ↓
Hosted LLM (Llama 3/GPT-4o)
 ↓
Response (Token Streaming)
```

Key aspects:
1. LangGraph for stateful session memory and multi-step reasoning.
2. Hybrid Search (Dense vector search + Sparse keyword search) to locate precise clauses.
3. Cohere Cross-Encoder Reranker to filter context.
4. Prompt caching and semantic cache layers to manage costs and latency.
5. Multi-tenant access controls for private legal documents.


System Design & Scenario-Based

Design a RAG chatbot for 10 million enterprise documents.
User asks a question but retrieval returns irrelevant chunks. How would you debug?
Design a legal document assistant with citation support.
How would you reduce hallucinations in a financial RAG system?
Design a customer support AI using company knowledge base.
Chunk size is causing poor answers. How would you optimize it?
Design a multilingual RAG system.
How would you implement Hybrid Search (BM25 + Vector Search)?
Design a GraphRAG architecture for connected knowledge.
How would you handle document updates in real-time?
Design a RAG system for healthcare records.
User asks questions across multiple PDFs. How would you preserve context?
Design a RAG pipeline for scanned PDFs and images.
Retrieval latency exceeds 2 seconds. How would you optimize?
Design a RAG system with source attribution.
How would you evaluate retrieval quality?
Design a RAG system supporting 1M daily users.
How would you prevent confidential data leakage?
Design semantic caching for a RAG application.
Long-context model vs RAG: which would you choose and why?
Design an autonomous travel planning agent.
Design an AI recruiter agent that screens candidates.
Build a coding assistant agent with GitHub integration.
Design a research agent that searches, summarizes and cites sources.
Design a customer support agent that can execute refunds.
How would you implement agent memory?
Design an agent capable of booking flights and hotels.
How would you prevent infinite agent loops?
Design a multi-step reasoning agent for tax advisory.
Design an AI project manager agent.
How would you implement tool selection?
Design an email triage agent.
Design a sales outreach agent.
How would you handle agent failures?
Design a self-correcting agent using Reflection Pattern.
Design an AI agent for stock market research.
How would you enforce agent guardrails?
Design an AI agent with long-term memory.
Design an autonomous workflow execution agent.
Agent vs Workflow Automation: when would you use each?
Design a multi-agent software development team.
Design a planner-executor-reviewer architecture.
Design a multi-agent customer support platform.
When would you use multiple agents instead of one?
Design an AI investment advisory team.
How would agents communicate with each other?
Design conflict resolution among agents.
Design agent orchestration using LangGraph.
Design a supervisor agent architecture.
How would you evaluate multi-agent performance?
Design ChatGPT for 100M users.
How would you reduce inference cost by 50%?
Design a token-efficient architecture.
Design LLM serving on Kubernetes.
Design multi-region LLM deployment.
How would you implement KV-cache optimization?
Design load balancing for LLM requests.
Design a fallback model strategy.
How would you optimize GPU utilization?
Design an LLM platform supporting multiple models.
Design an evaluation framework for RAG.
How would you measure hallucination rate?
Design online vs offline evaluation.
How would you evaluate agent quality?
Design A/B testing for prompts.
Design observability for LLM applications.
How would you monitor model drift?
Design tracing for agent execution.
How would you identify retrieval failures?
Design a human-in-the-loop review system.
Design a safe enterprise chatbot.
How would you prevent prompt injection attacks?
Design guardrails for an AI banking assistant.
Design role-based access control in RAG.
How would you secure tool-calling agents?
Design compliance architecture for healthcare AI.
How would you detect jailbreak attempts?
Design data governance for GenAI.
Design AI audit logging.
How would you implement responsible AI controls?
When would you choose Fine-Tuning over RAG?
Design a domain-specific medical chatbot.
How would you fine-tune with limited data?
Design a LoRA-based fine-tuning pipeline.
How would you avoid catastrophic forgetting?
Design continual learning architecture.
Fine-tuning vs Prompt Engineering tradeoffs?
Design a custom LLM for legal documents.
How would you evaluate a fine-tuned model?
Design model versioning and rollback.
Design ChatGPT from scratch.
Design GitHub Copilot.
Design Perplexity AI.
Design an AI-powered search engine.
Design Google NotebookLM.
Design an AI coding interviewer.
Design a real-time meeting summarization system.
Design a YouTube video understanding assistant.
Design an AI-powered tax advisor.
Design an autonomous software engineer agent.
