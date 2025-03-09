<!-- image -->

- Home
- Product news Product news See all product updates See all product updates

<!-- image -->

<!-- image -->

    - Android, Chrome &amp; Play

<!-- image -->

        - Android
        - Chrome
        - Chromebooks
        - Google Play
        - Wear OS
        - See all
- Platforms &amp; Devices

<!-- image -->

    - Fitbit
    - Google Nest
    - Pixel
    - See all
- Explore &amp; Get Answers

<!-- image -->

- Gemini
- Maps
- News
- Search
- Shopping
- See all
- Connect &amp; Communicate

<!-- image -->

- Classroom
- Photos
- Registry
- Translate
- In the Cloud

<!-- image -->

- Google Workspace
- More on the Cloud Blog
- Google Cloud
- See all

- Android, Chrome &amp; Play See all
    - Android
    - Chrome
    - Chromebooks
    - Google Play
    - Wear OS
- Platforms &amp; Devices See all

- Fitbit
- Google Nest
- Pixel
- Explore &amp; Get Answers See all

- Gemini
- Maps
- News
- Search
- Shopping
- Connect &amp; Communicate

- Classroom
- Photos
- Registry
- Translate
- In the Cloud See all

- Google Workspace
- More on the Cloud Blog
- Google Cloud
- Company news Company news

<!-- image -->

<!-- image -->

- Outreach &amp; initiatives

<!-- image -->

    - Arts &amp; Culture
    - Education
    - Entrepreneurs
    - Public Policy
    - Sustainability
    - See all
- Technology

<!-- image -->

- AI
- Developers
- Health
- Google DeepMind
- Google Labs
- Safety and security
- See all
- Inside Google

<!-- image -->

- Data centers and infrastructure
- Doodles
- Googlers
- Life at Google
- See all
- Around the globe

<!-- image -->

- Google in Asia
- Google in Europe
- Google in Latin America
- See all
- Authors

<!-- image -->

- Sundar Pichai, CEO
- Ruth Porat, President &amp; Chief Investment Officer
- Kent Walker, SVP
- James Manyika, SVP
- See all

- Outreach &amp; initiatives See all
    - Arts &amp; Culture
    - Education
    - Entrepreneurs
    - Public Policy
    - Sustainability
- Technology See all

- AI
- Developers
- Health
- Google DeepMind
- Google Labs
- Safety and security
- Inside Google See all

- Data centers and infrastructure
- Doodles
- Googlers
- Life at Google
- Around the globe See all

- Google in Asia
- Google in Europe
- Google in Latin America
- Authors See all

- Sundar Pichai, CEO
- Ruth Porat, President &amp; Chief Investment Officer
- Kent Walker, SVP
- James Manyika, SVP
- Feed

<!-- image -->

- Home
- Product news Product news See all product updates

<!-- image -->

<!-- image -->

    - Android, Chrome &amp; Play

<!-- image -->

        - Android
        - Chrome
        - Chromebooks
        - Google Play
        - Wear OS
        - See all
- Platforms &amp; Devices

<!-- image -->

    - Fitbit
    - Google Nest
    - Pixel
    - See all
- Explore &amp; Get Answers

<!-- image -->

- Gemini
- Maps
- News
- Search
- Shopping
- See all
- Connect &amp; Communicate

<!-- image -->

- Classroom
- Photos
- Registry
- Translate
- In the Cloud

<!-- image -->

- Google Workspace
- More on the Cloud Blog
- Google Cloud
- See all
- Company news Company news

<!-- image -->

<!-- image -->

- Outreach &amp; initiatives

<!-- image -->

    - Arts &amp; Culture
    - Education
    - Entrepreneurs
    - Public Policy
    - Sustainability
    - See all
- Technology

<!-- image -->

- AI
- Developers
- Health
- Google DeepMind
- Google Labs
- Safety and security
- See all
- Inside Google

<!-- image -->

- Data centers and infrastructure
- Doodles
- Googlers
- Life at Google
- See all
- Around the globe

<!-- image -->

- Google in Asia
- Google in Europe
- Google in Latin America
- See all
- Authors

<!-- image -->

- Sundar Pichai, CEO
- Ruth Porat, President &amp; Chief Investment Officer
- Kent Walker, SVP
- James Manyika, SVP
- See all
- Feed

- Press corner
- RSS feed

1. 
2. Technology
3. Research

# Meet Willow, our state-of-the-art quantum chip

Dec 09, 2024

[[read-time]] min read

Our new chip demonstrates error correction and performance that paves the way to a useful, large-scale quantum computer

## General summary

Google has developed a new quantum chip called Willow, which significantly reduces errors as it scales up, a major breakthrough in quantum error correction. Willow also performed a computation in under five minutes that would take a supercomputer 10 septillion years, demonstrating its potential for solving complex problems beyond the reach of classical computers. This achievement marks a significant step towards building commercially relevant quantum computers that can revolutionize fields like medicine, energy, and AI.

## Bullet points

Google's new quantum chip, Willow, is a major step towards building a useful, large-scale quantum computer.
Willow reduces errors exponentially as it scales up, achieving a breakthrough in quantum error correction.
Willow performed a benchmark computation in under five minutes that would take a supercomputer 10 septillion years.
Willow's performance is a sign that useful, very large quantum computers can be built.
Google is working on developing quantum algorithms that can solve real-world problems.

#### Explore other styles:

- General summary
- Bullet points

Today I’m delighted to announce Willow, our latest quantum chip. Willow has state-of-the-art performance across a number of metrics, enabling two major achievements.

- The first is that Willow can reduce errors exponentially as we scale up using more qubits. This cracks a key challenge in quantum error correction that the field has pursued for almost 30 years.
- Second, Willow performed a standard benchmark computation in under five minutes that would take one of today’s fastest supercomputers 10 septillion (that is, 1025) years — a number that vastly exceeds the age of the Universe.

The Willow chip is a major step on a journey that began over 10 years ago. When I founded Google Quantum AI in 2012, the vision was to build a useful, large-scale quantum computer that could harness quantum mechanics — the “operating system” of nature to the extent we know it today — to benefit society by advancing scientific discovery, developing helpful applications, and tackling some of society's greatest challenges. As part of Google Research, our team has charted a long-term roadmap, and Willow moves us significantly along that path towards commercially relevant applications.

## Exponential quantum error correction — below threshold!

Errors are one of the greatest challenges in quantum computing, since qubits, the units of computation in quantum computers, have a tendency to rapidly exchange information with their environment, making it difficult to protect the information needed to complete a computation. Typically the more qubits you use, the more errors will occur, and the system becomes classical.

Today in Nature, we published results showing that the more qubits we use in Willow, the more we reduce errors, and the more quantum the system becomes. We tested ever-larger arrays of physical qubits, scaling up from a grid of 3x3 encoded qubits, to a grid of 5x5, to a grid of 7x7 — and each time, using our latest advances in quantum error correction, we were able to cut the error rate in half. In other words, we achieved an exponential reduction in the error rate. This historic accomplishment is known in the field as “below threshold” — being able to drive errors down while scaling up the number of qubits. You must demonstrate being below threshold to show real progress on error correction, and this has been an outstanding challenge since quantum error correction was introduced by Peter Shor in 1995.

There are other scientific “firsts” involved in this result as well. For example, it’s also one of the first compelling examples of real-time error correction on a superconducting quantum system — crucial for any useful computation, because if you can’t correct errors fast enough, they ruin your computation before it’s done. And it’s a "beyond breakeven" demonstration, where our arrays of qubits have longer lifetimes than the individual physical qubits do, an unfakable sign that error correction is improving the system overall.

As the first system below threshold, this is the most convincing prototype for a scalable logical qubit built to date. It’s a strong sign that useful, very large quantum computers can indeed be built. Willow brings us closer to running practical, commercially-relevant algorithms that can’t be replicated on conventional computers.

## 10 septillion years on one of today’s fastest supercomputers

As a measure of Willow’s performance, we used the random circuit sampling (RCS) benchmark. Pioneered by our team and now widely used as a standard in the field, RCS is the classically hardest benchmark that can be done on a quantum computer today. You can think of this as an entry point for quantum computing — it checks whether a quantum computer is doing something that couldn’t be done on a classical computer. Any team building a quantum computer should check first if it can beat classical computers on RCS; otherwise there is strong reason for skepticism that it can tackle more complex quantum tasks. We’ve consistently used this benchmark to assess progress from one generation of chip to the next — we reported Sycamore results in October 2019 and again recently in October 2024.

Willow’s performance on this benchmark is astonishing: It performed a computation in under five minutes that would take one of today’s fastest supercomputers 1025 or 10 septillion years. If you want to write it out, it’s 10,000,000,000,000,000,000,000,000 years. This mind-boggling number exceeds known timescales in physics and vastly exceeds the age of the universe. It lends credence to the notion that quantum computation occurs in many parallel universes, in line with the idea that we live in a multiverse, a prediction first made by David Deutsch.

These latest results for Willow, as shown in the plot below, are our best so far, but we’ll continue to make progress.

Computational costs are heavily influenced by available memory. Our estimates therefore consider a range of scenarios, from an ideal situation with unlimited memory (▲) to a more practical, embarrassingly parallelizable implementation on GPUs (⬤).

<!-- image -->

Our assessment of how Willow outpaces one of the world’s most powerful classical supercomputers, Frontier, was based on conservative assumptions. For example, we assumed full access to secondary storage, i.e., hard drives, without any bandwidth overhead — a generous and unrealistic allowance for Frontier. Of course, as happened after we announced the first beyond-classical computation in 2019, we expect classical computers to keep improving on this benchmark, but the rapidly growing gap shows that quantum processors are peeling away at a double exponential rate and will continue to vastly outperform classical computers as we scale up.

## State-of-the-art performance

Willow was fabricated in our new, state-of-the-art fabrication facility in Santa Barbara — one of only a few facilities in the world built from the ground up for this purpose. System engineering is key when designing and fabricating quantum chips: All components of a chip, such as single and two-qubit gates, qubit reset, and readout, have to be simultaneously well engineered and integrated. If any component lags or if two components don't function well together, it drags down system performance. Therefore, maximizing system performance informs all aspects of our process, from chip architecture and fabrication to gate development and calibration. The achievements we report assess quantum computing systems holistically, not just one factor at a time.

We’re focusing on quality, not just quantity — because just producing larger numbers of qubits doesn’t help if they’re not high enough quality. With 105 qubits, Willow now has best-in-class performance across the two system benchmarks discussed above: quantum error correction and random circuit sampling. Such algorithmic benchmarks are the best way to measure overall chip performance. Other more specific performance metrics are also important; for example, our T1 times, which measure how long qubits can retain an excitation — the key quantum computational resource — are now approaching 100 µs (microseconds). This is an impressive ~5x improvement over our previous generation of chips. If you want to evaluate quantum hardware and compare across platforms, here is a table of key specifications:

Willow’s performance across a number of metrics.

<!-- image -->

## What’s next with Willow and beyond

The next challenge for the field is to demonstrate a first "useful, beyond-classical" computation on today's quantum chips that is relevant to a real-world application. We’re optimistic that the Willow generation of chips can help us achieve this goal. So far, there have been two separate types of experiments. On the one hand, we’ve run the RCS benchmark, which measures performance against classical computers but has no known real-world applications. On the other hand, we’ve done scientifically interesting simulations of quantum systems, which have led to new scientific discoveries but are still within the reach of classical computers. Our goal is to do both at the same time — to step into the realm of algorithms that are beyond the reach of classical computers and that are useful for real-world, commercially relevant problems.

Random circuit sampling (RCS), while extremely challenging for classical computers, has yet to demonstrate practical commercial applications.

<!-- image -->

We invite researchers, engineers, and developers to join us on this journey by checking out our open source software and educational resources, including our new course on Coursera, where developers can learn the essentials of quantum error correction and help us create algorithms that can solve the problems of the future.

<!-- image -->

My colleagues sometimes ask me why I left the burgeoning field of AI to focus on quantum computing. My answer is that both will prove to be the most transformational technologies of our time, but advanced AI will significantly benefit from access to quantum computing. This is why I named our lab Quantum AI. Quantum algorithms have fundamental scaling laws on their side, as we’re seeing with RCS. There are similar scaling advantages for many foundational computational tasks that are essential for AI. So quantum computation will be indispensable for collecting training data that’s inaccessible to classical machines, training and optimizing certain learning architectures, and modeling systems where quantum effects are important. This includes helping us discover new medicines, designing more efficient batteries for electric cars, and accelerating progress in fusion and new energy alternatives. Many of these future game-changing applications won’t be feasible on classical computers; they’re waiting to be unlocked with quantum computing.

- Research

### Related stories

- Health
Advancing healthcare and scientific discovery with AI

                  By
                  
                    
                    
                    Yossi Matias
                    

 Mar 04, 2025
- AI
The latest AI news we announced in February

                  By
                  
                    
                    
                    Keyword Team
                    

 Mar 03, 2025
- AI
The AI Action Summit: A golden age of innovation

                  By
                  
                    
                    
                    Sundar Pichai
                    

 Feb 10, 2025
- AI
The latest AI news we announced in January

                  By
                  
                    
                    
                    Keyword Team
                    

 Feb 05, 2025
- AI
2024: A year of extraordinary progress and advancement in AI

                  By
                  
                    
                    
                    Demis Hassabis
                    
                  
                    
                    &amp;
                    
                    
                    James Manyika
                    
                  
                    
                    &amp;
                    
                    
                    Jeff Dean
                    

 Jan 23, 2025
- AI
60 of our biggest AI announcements in 2024

                  By
                  
                    
                    
                    Keyword Team
                    

 Dec 23, 2024
- .

<!-- image -->

Let’s stay in touch. Get the latest news from Google in your inbox.

Follow Us

- 
- 
- 
- 
- 

- Privacy
- Terms
- About Google
- Google Products
- About the Keyword

- Help
- Bahasa Indonesia (Indonesia)
      

        Deutsch
      

        English
      

        English (Africa)
      

        English (Australia)
      

        English (Canada)
      

        English (India)
      

        English (MENA)
      

        Español (España)
      

        Español (Latinoamérica)
      

        Français (Canada)
      

        Français (France)
      

        Italiano
      

        Nederlands (Nederland)
      

        Polski
      

        Português (Brasil)
      

        Türkçe (Türkiye)
      

        Česko (Čeština)
      

        اللغة العربية (MENA)
      

        中文 (台灣)
      

        日本語 (日本)
      

        한국어