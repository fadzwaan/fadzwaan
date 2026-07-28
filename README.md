
## 🇲🇾 Malaysia at a Glance

> Live data sourced from [OpenDOSM](https://open.dosm.gov.my/) — Malaysia's official open statistics platform by the Department of Statistics Malaysia.

| Indicator | Value | Period | Value| Period |
|---|---|---|
| 👥 [Current Population](https://open.dosm.gov.my/dashboard/population) | **34.2 mil** | 1Q 2026 | | |
| 📈 [Economic Growth](https://open.dosm.gov.my/dashboard/gdp) | **5.4%** | 1Q 2026 | | |
| 💼 [Unemployment](https://open.dosm.gov.my/dashboard/labour-market) | **3.0%** | Apr 2026 | Increase Since Apr | |
| 🛒 [Inflation](https://open.dosm.gov.my/dashboard/consumer-prices) | **2.0%** | May 2026 | |  |
| 🏭 [Production Costs](https://open.dosm.gov.my/dashboard/producer-prices) | **+7.8%** | May 2026 | **9.2** | Jun 2026 |  
| 🔧 [Manufacturing Output](https://open.dosm.gov.my/dashboard/manufacturing-statistics) | **+9.1%** | Apr 2026 | **+8.9%** | Apr 2026 |
| ⚙️ [Industrial Production](https://open.dosm.gov.my/dashboard/industrial-production) | **+8.2%** | Apr 2026 | **+8.4%** | Apr 2026 |
| 🛍️ [Wholesale & Retail Trade](https://open.dosm.gov.my/dashboard/wholesale-retail-trade) | **+6.2%** | Apr 2026 | **3.1** | May 2026 | 

---

## 📚 Worth Reading

Interesting articles, papers, visualizations, and technical deep dives that I found valuable. Each entry includes a short personal takeaway or review.

### huggingface 

> Model Routing is Simple . Until It Isn't [read](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt)
routing is not about choosing model its about optimizing sistem. choosing model are one variable , more than that is caching behavior , inifrastructure state, compliance constraints and workloads patterns.
>  two new encoder models on Hugging Face: LFM2.5-Encoder-230M and LFM2.5-Encoder-350M. [here](https://huggingface.co/blog/LiquidAI/lfm2-5-encoders)



### thehackernews 
> TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development [read](https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html)
tuxbot a botnet shows signs of being developed with assistance from LLM. the generated code used in tuxbot include safety disclaimer that the developer failed to remove before shipping. Although the LLM clearly aided in constructing the botnet serveral functions in the analyzed samples failed to work correctly. the cybersecurity company said a manual code review would have resolved these errors and that its possible more polished interations of the malware exissts out there in the wild

> north korea uses SVG and embed virus in it as a payload in job advertisement to steal crypto [read](https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html)
> openai goes to JFROG and then found a cred and its way to huggingface [read](https://thehackernews.com/2026/07/jfrog-confirms-openai-models-exploited.html)



### kaggle
> QSAR biodegradation Data Set [read](https://www.kaggle.com/datasets/muhammetvarl/qsarbiodegradation)
biodegration is the natural process where microorganism break down complex organic materials into simple substances. Data set containing values for 41 attributes (molecular descriptors) used to classify 1055 chemicals into 2 classes (ready and not ready biodegradable).
> This dataset contains JSON replays of completed episodes from a Kaggle simulations competition. Replays are selected daily, ranked by average agent rating, and capped at 20 GiB per day. See manifest.csv for the list of included episodes and their scores. [read](https://www.kaggle.com/datasets/kaggle/pokemon-tcg-ai-battle-episodes-2026-07-26)





### arxiv

Trying to reconstruct the future option price (at maturity T) from current observed option prices by running the Black–Scholes equation forward in time. [link](https://arxiv.org/html/2606.12450v1)

Show weather using new probability modelling , [read](https://arxiv.org/html/2607.24596v1)

### cisco blog
Scale. Speed. Trust: Three Imperatives for the AI Era
The AI era is not just about smarter models — it requires a complete redesign of networking, security, and operations. Companies that modernize infrastructure will lead the next wave of innovation.
https://blogs.cisco.com/news/accelerating-the-pace-of-innovation-for-the-ai-era
> 80% of environment impact come during design phase , [read](https://blogs.cisco.com/our-corporate-purpose/sustainability-101-materials-at-the-center-of-sustainability-human-rights-and-business-resilience)


### git, docker, uv
> you can zip your commit [git archive](https://git-scm.com/docs/git-archive)
> you can check your config [git config](https://git-scm.com/docs/git-config) and unset your typo config for example git config --unset --global user.emal"
> you can git clone --filter=blob:none to not download blob file and use [git backfil](https://git-scm.com/docs/git-backfill) to safely install back the missing blob

> you can view resource usage with `docker container stats`
> you can view network known to Docker Engine with `docker network ls`


> you can keep your auth using `uv auth login google.com` and check the contents here `Get-Content "$env:APPDATA\uv\credentials\credentials.toml"`
> uv tree displays your project's dependency tree
