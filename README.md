## Tools
[threadsloom](https://threadloom-fp43fo6sk-fadzwans-projects.vercel.app)
## 🇲🇾 Malaysia at a Glance

> Live data sourced from [OpenDOSM](https://open.dosm.gov.my/) — Malaysia's official open statistics platform by the Department of Statistics Malaysia.

| Indicator | Value | Period | Value| Period |
|---|---|---|---|---|
| 👥 [Current Population](https://open.dosm.gov.my/dashboard/population) | **34.2 mil** | 1Q 2026 | 34.4 mil | 2Q 2026 |
| 📈 [Economic Growth](https://open.dosm.gov.my/dashboard/gdp) | **5.4%** | 1Q 2026 | 5.4% | 1Q 2026 |
| 💼 [Unemployment](https://open.dosm.gov.my/dashboard/labour-market) | **3.0%** | Apr 2026 | 3.0% | May 2026|
| 🛒 [Inflation](https://open.dosm.gov.my/dashboard/consumer-prices) | **2.0%** | May 2026 | 1.9% | Jun 2026 |
| 🏭 [Production Costs](https://open.dosm.gov.my/dashboard/producer-prices) | **+7.8%** | May 2026 | **9.2** | Jun 2026 |  
| 🔧 [Manufacturing Output](https://open.dosm.gov.my/dashboard/manufacturing-statistics) | **+9.1%** | Apr 2026 | **+8.9%** | May 2026 |
| ⚙️ [Industrial Production](https://open.dosm.gov.my/dashboard/industrial-production) | **+8.2%** | Apr 2026 | **+8.4%** | May 2026 |
| 🛍️ [Wholesale & Retail Trade](https://open.dosm.gov.my/dashboard/wholesale-retail-trade) | **+6.2%** | Apr 2026 | **3.1** | May 2026 | 

---

## 📚 Worth Reading

Interesting articles, papers, visualizations, and technical deep dives that I found valuable. Each entry includes a short personal takeaway or review.

### huggingface 

> Model Routing is Simple . Until It Isn't [read](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt)
routing is not about choosing model its about optimizing sistem. choosing model are one variable , more than that is caching behavior , inifrastructure state, compliance constraints and workloads patterns.
>  two new encoder models on Hugging Face: LFM2.5-Encoder-230M and LFM2.5-Encoder-350M. [here](https://huggingface.co/blog/LiquidAI/lfm2-5-encoders)
> managing GPU is like managing aviation [here](https://huggingface.co/blog/Dharma-AI/gpu-management]

> this is cool but  i just notice there are multiple type of benchmark here [read](https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b)

### thehackernews 
> TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development [read](https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html)
tuxbot a botnet shows signs of being developed with assistance from LLM. the generated code used in tuxbot include safety disclaimer that the developer failed to remove before shipping. Although the LLM clearly aided in constructing the botnet serveral functions in the analyzed samples failed to work correctly. the cybersecurity company said a manual code review would have resolved these errors and that its possible more polished interations of the malware exissts out there in the wild

> north korea uses SVG and embed virus in it as a payload in job advertisement to steal crypto [read](https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html)
> openai goes to JFROG and then found a cred and its way to huggingface [read](https://thehackernews.com/2026/07/jfrog-confirms-openai-models-exploited.html)
> this further backed fatwa on bitcoin being haram, cause as simple as coldcard wallet can lead to bitcoin being stolen [read](https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html)
>

> just dont use Rovo anymore [read](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)



### kaggle
> QSAR biodegradation Data Set [read](https://www.kaggle.com/datasets/muhammetvarl/qsarbiodegradation)
biodegration is the natural process where microorganism break down complex organic materials into simple substances. Data set containing values for 41 attributes (molecular descriptors) used to classify 1055 chemicals into 2 classes (ready and not ready biodegradable).
> This dataset contains JSON replays of completed episodes from a Kaggle simulations competition. Replays are selected daily, ranked by average agent rating, and capped at 20 GiB per day. See manifest.csv for the list of included episodes and their scores. [read](https://www.kaggle.com/datasets/kaggle/pokemon-tcg-ai-battle-episodes-2026-07-26)
>  This dataset simulates transactions from a digital wallet platform similar to popular services like PayTm in India or Khalti in Nepal. It contains 5000 synthetic records of various financial transactions across multiple categories, providing a rich source for analysis of digital payment behaviors and trends.[read](https://www.kaggle.com/datasets/harunrai/digital-wallet-transactions/data)





### arxiv

Trying to reconstruct the future option price (at maturity T) from current observed option prices by running the Black–Scholes equation forward in time. [link](https://arxiv.org/html/2606.12450v1)

Show weather using new probability modelling , [read](https://arxiv.org/html/2607.24596v1)

### cisco blog
Scale. Speed. Trust: Three Imperatives for the AI Era
The AI era is not just about smarter models — it requires a complete redesign of networking, security, and operations. Companies that modernize infrastructure will lead the next wave of innovation.
https://blogs.cisco.com/news/accelerating-the-pace-of-innovation-for-the-ai-era
> 80% of environment impact come during design phase , [read](https://blogs.cisco.com/our-corporate-purpose/sustainability-101-materials-at-the-center-of-sustainability-human-rights-and-business-resilience)
> uh stop micromanage your people eh your hardware, [read](https://blogs.cisco.com/networking/wireless-isnt-magic-its-just-better-when-you-stop-micromanaging-your-network)
> I have been closely associated w/ IB  vs Ethernet since early VMware days. While the appeal of low latency aspect of IB is there, Ethernet has always gotten better overtime, and better at solving problems at scale. Especially with concepts around MRC, etc, it can show some real power.  IB keeps introducing things that existing protocols have solved for many years. I am not anti-IB or any, just stating the simpification that ethernet offers. Having said, I haven't been looking at this space in recent times, so more to learn. [read](https://blogs.cisco.com/datacenter/scaling-the-future-why-ethernet-is-the-backbone-of-ai-supercomputing)




### git, docker, uv
> you can zip your commit [git archive](https://git-scm.com/docs/git-archive)
> you can check your config [git config](https://git-scm.com/docs/git-config) and unset your typo config for example git config --unset --global user.emal"
> you can git clone --filter=blob:none to not download blob file and use [git backfil](https://git-scm.com/docs/git-backfill) to safely install back the missing blob
> git notes add -m "Tested REE calculation interface on Surface Pro 7. Verified patient input and prediction history."

> you can view resource usage with `docker container stats`
> you can view network known to Docker Engine with `docker network ls`
> Avoid production Dockerfiles like:

RUN apt update
RUN apt install curl
RUN apt install vim
RUN apt install git

The more stuff you put inside the runtime image, the larger the attack surface becomes.

Docker's hardened images intentionally remove things such as shells, package managers, compilers and debugging tools from production variants. Thats why multi stage deployments is important

BUILD IMAGE
    │
    ├── compiler
    ├── pip
    ├── build dependencies
    └── development tools
             │
             ▼
       application
             │
             ▼
RUNTIME IMAGE
    │
    ├── application
    ├── required libraries
    └── nothing unnecessary

docker dhi is a Docker CLI for managing Docker Hardened Images (DHI).


> you can keep your auth using `uv auth login google.com` and check the contents here `Get-Content "$env:APPDATA\uv\credentials\credentials.toml"`
> uv tree displays your project's dependency tree
> uv cheatlist , [read](https://mathspp.com/blog/uv-cheatsheet)
