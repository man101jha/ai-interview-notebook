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

How do generators and `yield` work? How are they useful in AI applications?
How do decorators work in Python? How do you write a decorator that accepts arguments?
Explain the context manager protocol and how it applies to resource management?
What is the GIL (Global Interpreter Lock)? How does it affect multi-threading vs. multi-processing vs. asyncio?
How does `asyncio` achieve concurrency under the hood?
What are metaclasses, and how do they differ from class decorators?
How does Python manage memory, and how do you prevent leaks in RAG systems?
Explain dunder (magic) methods and when you would implement them.
Why is type hinting critical in AI codebases? What are Annotated, Union, and Generic?
Compare Python dataclasses vs. Pydantic models. When do you use each?
What is the difference between `is` and `==`? Under what conditions can `is` behave unexpectedly?
Why are mutable default arguments dangerous in Python, and how do you fix them?
What is the output of `list_val = [[0]] * 3`? Explain why modifying `list_val[0][0]` changes other elements.
Why can `x = x + [1]` behave differently than `x += [1]` in Python lists?
Explain late binding in Python closures and how it can cause unexpected outputs inside loops.
What is the difference between a shallow copy and a deep copy? When is each necessary?
Why can a `finally` block override a `return` statement in Python?
Explain the difference between class variables and instance variables. How can dynamic mutation cause bugs?
What is name mangling in Python, and why does it matter?
What is the difference between `dict.get(key)` and indexing `dict[key]`? When should you use each?
Explain how arguments are passed in Python. Is it pass-by-value or pass-by-reference?
What are Python namespaces, and what is the LEGB rule for scope resolution?
What is Method Resolution Order (MRO) in Python, and how is it calculated for multiple inheritance?
What are descriptors in Python, and how do they enable properties (`@property`) under the hood?
What are `__slots__` in Python classes, and how do they improve performance and memory usage?
What is the difference between `__new__` and `__init__` methods in class instantiation?
How does NumPy leverage vectorization and memory layouts (C-contiguous vs Fortran-contiguous) for speed?
How are NumPy arrays advantageous over Python lists? Explain in terms of memory layout and CPU caching.
How does Pandas handle missing values under the hood (e.g. NaN, None), and how do you handle them memory-safely?
What is the difference between a module and a package in Python? How does relative import syntax work?


FastAPI

Explain how to implement custom request validation and serialization beyond Pydantic defaults.
How do you design FastAPI microservices and handle inter-service communication?
What strategies do you use for caching in FastAPI applications?
How do you deploy a FastAPI application with Docker and Uvicorn/Gunicorn?
Explain lifespan events (startup/shutdown) in FastAPI and their use cases.
How do you implement rate limiting and request throttling in FastAPI?
What is middleware in FastAPI and how do you create custom middleware?
How do you write tests for FastAPI applications using TestClient?
How do you implement CORS (Cross-Origin Resource Sharing) in FastAPI?
How do you connect FastAPI with a database using SQLAlchemy?
How do you handle errors and exceptions in FastAPI? Explain HTTPException.
What is Dependency Injection in FastAPI, and how does it work?
How do you handle database migrations in FastAPI using Alembic?
Explain APIRouter and how to structure a large FastAPI application.
How do you implement WebSockets in FastAPI for real-time communication?
What are Background Tasks in FastAPI, and when should you use them?
How do you implement OAuth2 with JWT authentication in FastAPI?
Explain async and await in FastAPI. When should you use async def vs def?
What is the purpose of response_model in FastAPI path operations?
How do you handle form data and file uploads in FastAPI?
Explain the different HTTP methods and their usage in FastAPI.
How do you define request body using Pydantic models?
What are path parameters and query parameters in FastAPI? How do you define them?
How do you create a basic FastAPI application with a GET endpoint?
What is FastAPI, and what are its key features?
Compare FastAPI with Flask and Django REST Framework.
How does FastAPI automatically generate OpenAPI (Swagger) documentation?
What is Pydantic, and why is it integral to FastAPI?
What is Starlette, and how does FastAPI build upon it?
Explain the difference between ASGI and WSGI. Why does FastAPI use ASGI?


Resume-Based Questions
Tell me about Nyaya-Pro. Why did you choose FAISS instead of a managed vector database like Pinecone?
What was the role of the agentic query router in Nyaya-Pro? How does it classify and dispatch queries?
Why did you use a semantic cross-encoder reranker in Nyaya-Pro? How did it affect latency?
Explain your multi-agent CrewAI pipeline in JobPilot AI. How do the agents collaborate?
In JobPilot AI, why did you use Ollama locally for development but Groq API in production?
How does ExamGenie AI parse study PDFs and generate interactive MCQs? How do you prevent hallucinations?
You worked at Yotta Infrastructures as a Senior Software Developer. How did you optimize the CCTV live-playback streams?
How did you improve dashboard performance by 30% using NgRx in OneYotta Portal?
How did you handle authentication in OneYotta Portal using Keycloak and Azure AD?
How do you balance your strong frontend background (Angular, Flutter) with your transition into AI Engineering?
