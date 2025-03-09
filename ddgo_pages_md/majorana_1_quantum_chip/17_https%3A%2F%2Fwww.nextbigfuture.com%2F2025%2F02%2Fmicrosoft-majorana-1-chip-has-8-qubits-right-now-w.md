<!-- image -->

<!-- image -->

- Artificial intelligence
- Superconductor
- Humanoid Robot
- Science
- About
    - Contact
    - About
    - Privacy Policy
    - Terms and Conditions

Home » Artificial intelligence » Microsoft Majorana 1 Chip Has 8 Qubits Right Now with a Roadmap to 1 Million Raw Qubits

<!-- image -->

<!-- image -->

# Microsoft Majorana 1 Chip Has 8 Qubits Right Now with a Roadmap to 1 Million Raw Qubits

Microsoft team behind the recent breakthrough in physics and quantum computing demonstrated by the new Majorana 1 chip, engineered from an entirely new material that has the potential to scale to millions of qubits on a single chip.

Microsoft today introduced Majorana 1, the world’s first quantum chip powered by a new Topological Core architecture that it expects will realize quantum computers capable of solving meaningful, industrial-scale problems in years, not decades.

QuEra, Quantinuum and Quantum Circuits are in the lead with error corrected or fast error detecting quantum systems. We are still 4-8 years away from major error corrected quantum systems that might make a big computing difference for some kinds of problems.

Microsoft leverages the world’s first topoconductor, a breakthrough type of material which can observe and control Majorana particles to produce more reliable and scalable qubits, which are the building blocks for quantum computers.

The Microsoft Majorana 1 chip currently has 8 qubits. These are topological qubits, which are designed to be more stable and less prone to errors compared to traditional qubits, thanks to their unique properties based on Majorana zero modes.

Microsoft has outlined an ambitious roadmap to scale up to 1 million qubits on a single chip. This significant jump from 8 qubits is made feasible by their new architecture, which leverages the inherent stability of topological qubits. The company believes this approach provides a clear path to fitting a million qubits onto a single chip, a claim supported by the enhanced error resistance of their qubit design.

Regarding whether these 1 million qubits would be logical qubits or raw qubits:

Raw qubits refer to the physical qubits on the chip.

    Logical qubits are error-corrected qubits capable of reliable computations, typically requiring multiple raw qubits for error correction.

Microsoft’s roadmap appears to focus on scaling to 1 million raw qubits. The stability of their topological qubits—often likened to a knot in a rope that stays in place even when disturbed—suggests that these raw qubits have built-in error resistance at the hardware level. This could reduce the number of additional raw qubits needed for error correction. Microsoft’s approach simplifies quantum error correction through a measurement-based method using digital pulses, further supporting the idea that the 1 million figure refers to raw qubits with enhanced stability.

However, for practical quantum computing, logical qubits are essential to ensure reliable and accurate computations. Even with 1 million raw qubits, Microsoft would still need to implement error correction to create a smaller number of logical qubits from these raw ones. The exact number of logical qubits achievable would depend on the efficiency of their error-correction techniques, which is not fully detailed in the available information.

Logical Error Corrected Qubit Estimates – Error corrected Are More Important Than More Raw Qubits

While exact numbers are still under investigation, research suggests that topological qubits could significantly reduce the ratio of raw qubits to logical qubits compared to traditional methods:

Theoretical estimates: In ideal scenarios, with high-fidelity topological operations and strong topological protection, some studies propose that the ratio could be as low as 2 to 10 raw qubits per logical qubit.

Practical expectations: Accounting for real-world imperfections, more conservative estimates suggest a ratio closer to 10 to 50 raw qubits per logical qubit. This is still a substantial improvement over traditional quantum error correction schemes, which often require 100–1,000 raw qubits per logical qubit, and possibly even dual-rail qubits, which might require about 20 raw qubits per logical qubit.

Besides error correction there is how many operations can be performed. Like how many steps of an algorithm.

Who is in the Lead?

QuEra Computing

QuEra, a pioneer in neutral atom technology, has achieved a notable milestone in collaboration with Harvard University. In December 2023, they demonstrated 48 logical qubits using 280 physical qubit, executing large-scale algorithms on an error-corrected quantum computer. This demonstration included high-fidelity operations, such as a two-qubit transversal CNOT gate with a fidelity of 0.9993, and a circuit error rate of 0.002 with eight logical qubits—11 times better than their physical qubit error rate of 0.023. QuEra’s roadmap aims for 100 logical qubits by 2026, but their current record stands at 48 logical qubits, making it a significant achievement in the field.

Quantinuum

Quantinuum, a leader in trapped ion technology, has made significant strides with its H-Series quantum computers. In collaboration with Microsoft, Quantinuum demonstrated 12 logical qubits using ion-trap hardware, achieving an impressive 800-fold reduction in error rates compared to physical qubits. This milestone highlights the high reliability of their logical qubits, making them suitable for fault-tolerant computations. Additionally, in December 2024, Quantinuum announced entangling 50 logical qubits in a specific experiment, creating a Greenberger-Horne-Zeilinger (GHZ) state. However, this appears to be a specialized benchmark rather than an indication of 50 fully operational logical qubits for general use. For practical computations, their demonstrated capacity remains at 12 logical qubits.

Quantum Circuits has error detecting qubits.

They use a superconducting system uses cylindrical chambers that confine a single microwave frequency photon. They use RF frequencies to control the movement and actions of the photon. A coupler connecting the two chambers is used to transfer the photon between the chambers. Currently, the chambers each have a diameter of 5 millimeters. They will shrink those down to microscopic size in later generations. Superconducting Dual Resonator Qubits enhance the fidelity of quantum applications with error detection and correction.

There are two superconducting resonators (aka cavities) connected by a so-called “coupler.”

Quantum Circuits’ error-detecting dual-rail qubits innovation allows errors to be detected and corrected first to avoid disrupting performance at scale. This system will enable about 10-20 physical quantum qubits instead of 200 physical qubits for each error correct logical qubit.

PsiQuantum

PsiQuantum is developing a photonic quantum computer with an ambitious goal of reaching 1 million qubits. While this target is promising, their technology is still in the development phase, and they have not yet announced any operational quantum computers or demonstrated logical qubits. As a result, PsiQuantum currently has 0 logical qubits in terms of proven achievements.

Other companies like IBM, Google, and IonQ have not yet reported logical qubit counts that rival QuEra or Quantinuum. This microsoft work is not talking about a logical error corrected qubit yet.

2033 Goal for Utility Scale Quantum Computing

DARPA has selected and is in negotiations with Microsoft and PsiQuantum for the Validation and Co-Design stage of the Underexplored Systems for Utility-Scale Quantum Computing (US2QC) program, one of two programs that make up DARPA’s larger Quantum Benchmarking Initiative (QBI).

DARPA’s Quantum Benchmarking Initiative (QBI) aims to determine whether it’s possible to build an industrially useful quantum computer much faster than conventional predictions. Specifically, QBI is designed to rigorously verify and validate whether any quantum computing approach can achieve utility-scale operation — meaning its computational value exceeds its cost — by the year 2033.

New Superconductor-Semiconductor for Majorana Chips

In the same way that the invention of semiconductors made today’s smartphones, computers and electronics possible, topoconductors and the new type of chip they enable offer a path to developing quantum systems that can scale to a million qubits and are capable of tackling the most complex industrial and societal problems, Microsoft said.

This new architecture used to develop the Majorana 1 processor offers a clear path to fit a million qubits on a single chip that can fit in the palm of one’s hand, Microsoft said. This is a needed threshold for quantum computers to deliver transformative, real-world solutions – such as breaking down microplastics into harmless byproducts or inventing self-healing materials for construction, manufacturing or healthcare. All the world’s current computers operating together can’t do what a one-million-qubit quantum computer will be able to do.

Microsoft’s topological qubit architecture has aluminum nanowires joined together to form an H. Each H has four controllable Majoranas and makes one qubit. These Hs can be connected, too, and laid out across the chip like so many tiles.

“It’s complex in that we had to show a new state of matter to get there, but after that, it’s fairly simple. It tiles out. You have this much simpler architecture that promises a much faster path to scale,” said Krysta Svore, Microsoft technical fellow.

Chapters:

0:00 – Introducing Majorana 1

1:26 – Why does quantum computing matter?

2:47 – Qubits, the building blocks of quantum computing

5:05 – Understanding the topological state

7:00 – How the Majorana 1 chip works

9:10 – How quantum and classical computing work together

10:13 – The Quantum Age

The topoconductor, or topological superconductor, is a special category of material that can create an entirely new state of matter – not a solid, liquid or gas but a topological state. This is harnessed to produce a more stable qubit that is fast, small and can be digitally controlled, without the tradeoffs required by current alternatives. A new paper published Wednesday in Nature outlines how Microsoft researchers were able to create the topological qubit’s exotic quantum properties and also accurately measure them, an essential step for practical computing.

This breakthrough required developing an entirely new materials stack made of indium arsenide and aluminum, much of which Microsoft designed and fabricated atom by atom. The goal was to coax new quantum particles called Majoranas into existence and take advantage of their unique properties to reach the next horizon of quantum computing, Microsoft said.

The world’s first Topological Core powering the Majorana 1 is reliable by design, incorporating error resistance at the hardware level making it more stable.

Commercially important applications will also require trillions of operations on a million qubits, which would be prohibitive with current approaches that rely on fine-tuned analog control of each qubit. The Microsoft team’s new measurement approach enables qubits to be controlled digitally, redefining and vastly simplifying how quantum computing works.

Microsoft has partnered with Quantinuum and Atom Computing to reach scientific and engineering breakthroughs with today’s qubits, including the announcement last year of the industry’s first reliable quantum computer.

The quantum chip doesn’t work alone. It exists in an ecosystem with control logic, a dilution refrigerator that keeps qubits at temperatures much colder than outer space and a software stack that can integrate with AI and classical computers. All those pieces exist, built or modified entirely in-house, she said.

To be clear, continuing to refine those processes and getting all the elements to work together at accelerated scale will require more years of engineering work. But many difficult scientific and engineering challenges have now been met, Microsoft said.

Getting the materials stack right to produce a topological state of matter was one of the hardest parts, Svore added. Instead of silicon, Microsoft’s topoconductor is made of indium arsenide, a material currently used in such applications as infrared detectors and which has special properties. The semiconductor is married with superconductivity, thanks to extreme cold, to make a hybrid.

“We are literally spraying atom by atom. Those materials have to line up perfectly. If there are too many defects in the material stack, it just kills your qubit,” Svore said.

Nature- Interferometric single-shot parity measurement in InAs–Al hybrid devices

Abstract

The fusion of non-Abelian anyons is a fundamental operation in measurement-only topological quantum computation1. In one-dimensional topological superconductors (1DTSs) fusion amounts to a determination of the shared fermion parity of Majorana zero modes (MZMs). Here we introduce a device architecture5 that is compatible with future tests of fusion rules. We implement a single-shot interferometric measurement of fermion parity  in indium arsenide–aluminium heterostructures with a gate-defined superconducting nanowire. The interferometer is formed by tunnel-coupling the proximitized nanowire to quantum dots. The nanowire causes a state-dependent shift of the quantum capacitance of these quantum dots of up to 1 fF. Our quantum-capacitance measurements show flux h/2e-periodic bimodality with a signal-to-noise ratio (SNR) of 1 in 3.6 microseconds at optimal flux values. From the time traces of the quantum-capacitance measurements, they extract a dwell time in the two associated states that is longer than 1 ms at in-plane magnetic fields of approximately 2 T. They discuss the interpretation of their measurements in terms of both topologically trivial and non-trivial origins. The large capacitance shift and long poisoning time enable a parity measurement with an assignment error probability of 1%.

They have presented dispersive gate-sensing measurements of the quantum capacitance in InAs–Al hybrid devices using a system architecture that can be adapted to other materials platforms. After tuning the nanowire density and in-plane magnetic field into the parameter regime identified by the TGP14 and balancing the interferometer formed by the nanowire and the quantum dots, we observed a flux-dependent bimodal RTS in the quantum capacitance, which we interpret as switches of the parity of a fermionic state in the wire. They have fit these data to a model in which the fermion parity is associated with two MZMs localized at the opposite ends of a 1DTS and find good agreement. These measurements do not, by themselves, determine whether the low-energy states detected by interferometry are topological. However, our data tightly constrain the allowable energy splittings in models of trivial Andreev states.

In conclusion, their findings represent substantial progress towards the realization of a topological qubit based on measurement-only operations. Single-shot fermion parity measurements are a key requirement for a Majorana-based topological quantum computation architecture.

<!-- image -->

<!-- image -->

Brian Wang is a Futurist Thought Leader and a popular Science blogger with 1 million readers per month. His blog Nextbigfuture.com is ranked #1 Science News Blog. It covers many disruptive technology and trends including Space, Robotics, Artificial Intelligence, Medicine, Anti-aging Biotechnology, and Nanotechnology.

Known for identifying cutting edge technologies, he is currently a Co-Founder of a startup and fundraiser for high potential early-stage companies. He is the Head of Research for Allocations for deep technology investments and an Angel Investor at Space Angels.

A frequent speaker at corporations, he has been a TEDx speaker, a Singularity University speaker and guest at numerous interviews for radio and podcasts.  He is open to public speaking and advising engagements.

## 8 thoughts on “Microsoft Majorana 1 Chip Has 8 Qubits Right Now with a Roadmap to 1 Million Raw Qubits”

1. Robert C 

 
										February 22, 2025 at 2:50 pm									
 

I’m very impressed. Question: How do they connect/integrate it into our current technology?
Reply
2. Robert C 

 
										February 22, 2025 at 2:28 pm									
 

The “problem” I see with QM technology, is it’s ability to integrate with the technology we have today. Dealing with a 1and0 world, becomes much more “awkward” when “1and0” happen at the same time. Our current technology, can not deal with it. No matter how fast your “adding machine” is, it can’t deal with concepts it was never designed to “compute”. Both QM based computers, and biological informatics operate on principles simple digital computers, do not. I don’t have an answer to this problem, but if may make an observation?
Artificial prosthetics that involve electronics, have long had a “problem” connecting with the person there attached to. Our current technology, and biology just don’t work the same. Makes it very hard for our limited technology, to integrate with us. What I have read, is if an electrical system can “pause and absorb” data from human muscles for just a few milliseconds, it will better react to what human muscles actually do. Electrical systems operate must faster then we do. But we are much more adaptable and robust. We take our time, but only by a few milliseconds. It’s connecting the dots between technologies, that make’s it work.
I think that’s one way to make quantum mechanic technology work for us. We need to connect the dots.
Reply
3. Jim Takchess 

 
										February 22, 2025 at 6:17 am									
 

https://www.wsj.com/science/physics/microsoft-quantum-computing-physicists-skeptical-d3ec07f0?st=pemYah.    Wsj published this today
Reply
4. dumpster4 

 
										February 21, 2025 at 9:45 am									
 

But can it borrow computing power from different universes?        🙂
“Google Quantum AI founder Hartmut Neven wrote in his blog post that this chip was so mind-boggling fast that it must have borrowed computational power from other universes.
Ergo the chip’s performance indicates that parallel universes exist and “we live in a multiverse.””
Source:
https://techcrunch.com/2024/12/10/google-says-its-new-quantum-chip-indicates-that-multiple-universes-exist/
Reply
5. Jim Takchess 

 
										February 21, 2025 at 7:01 am									
 

Thanks Brian,

Recenting I read Computing with Quantum Cats which was a good intro though dated book on QC. Does anyone have recommendations on a more recent popular book on QC ? Thanks
Reply
6 Karl February 20, 2025 at 6:17 pm “in years, not decades” Shouldn’t the statement rather be closer to “minutes not millenia”Isn’t that the real essance of quantum compute ?I’m more interested in the multi thousand qbit impact on the AI learning process as it would speed that stage up to real time. Reply .children

<!-- image -->

<!-- image -->

“in years, not decades” Shouldn’t the statement rather be closer to “minutes not millenia”

Isn’t that the real essance of quantum compute ?

I’m more interested in the multi thousand qbit impact on the AI learning process as it would speed that stage up to real time.

    - Researcher February 20, 2025 at 6:44 pm “Microsoft today introduced … a new Topological Core architecture that it expects will realize quantum computers capable of solving meaningful, industrial-scale problems in years, not decades.“ In that sentence, “years” refers to “realize”, not “solving”. They’re saying that they will be able to build a useful machine in years rather than decades. My guess would be that a machine capable of breaking useful cryptography might be on the order of 10 years away, which would count as years rather than decades. But there are still a number of surprises that might happen to delay that. Or accelerate it. I guess we’ll see. Reply .children

<!-- image -->

<!-- image -->

“Microsoft today introduced … a new Topological Core architecture that it expects will realize quantum computers capable of solving meaningful, industrial-scale problems in years, not decades.“

In that sentence, “years” refers to “realize”, not “solving”.  They’re saying that they will be able to build a useful machine in years rather than decades.

My guess would be that a machine capable of breaking useful cryptography might be on the order of 10 years away, which would count as years rather than decades. But there are still a number of surprises that might happen to delay that. Or accelerate it. I guess we’ll see.

        - Researcher 

 
										February 20, 2025 at 6:47 pm									
 

Also, it isn’t obvious that a quantum computer could speed up AI at all. It wouldn’t be able to speed up the training of the current LLM architecture. There have been proposals for other kinds of AI that might benefit from a quantum computer. But no one knows whether those kinds of AI would be useful. The only way to know is to try it. Which can’t really be done until we have giant quantum computers.
Reply

### Leave a Comment Cancel reply

Comment

## Categories

## Recent Posts

- Sina Finance is Reporting Imminent Tesla China FSD Rollout
- Poland Clone Robotics Make Liquid Muscled Synthetic Copy of the Human Body
- Anthropic Releases Claude 3.7 Sonnet a Reasoning Model
- Overcoming Constraints and Limits to Scaling AI
- What Have Grandmasters Learned from Superintelligent Chess Programs?