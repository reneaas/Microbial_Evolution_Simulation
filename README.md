# Microbial_Evolution_Simulation

A simplified simulation of the evolution of microbes in a petridish.

## The model
The model consists of a few simplified assumptions to represent real-life properties. These include:

1. A genome consisting of 8 genes. The genome only influences the microbe's decision as to which direction
it shall move from a given position.
2. A set of parameters definining its ability to reproduce and survive. These include:
	- A minimum energy threshold that must be reached to reproduce.
	- A minimum age before reproduction can take place.
	- A maximum energy content that the microbe can sustain at any given time. 
3. Food distribution, from say a smaller bacterium, which is distributed at finite time intervals according to
some prespecified distribution.
4. During reproduction, there's a probability that the offspring directly inherits the genes of its parent microbe. Otherwise a new genome is randomly generated.


## The food distribution
The current food distributions in the model is
- Uniform food distribution. The food is distributed a regular intervals with uniform distribution across the entire petridish. 
- "Garden of Eden" distribution. Food is still distributed uniformly at regular time intervals. In addition, a larger abundance of food is distributed in a small area at the center of the petridish. 

## Does evolution occur in the simulation? 
The short answer is yes, for both food distribution conditions. 

- Uniform food distribution: The genomes that on average makes the microbes move in longer straight paths, only turning on occasion, survives while microbes that tend to move around with a smaller area coverage tend to consume all the local food before it is replenished, and thus dies. Natural selection thus favors longer paths.
- "Garden of Eden" distribution. Here the microbes that move in straight paths with occasional turns survive outside of the "Garden of Eden". While microbes that tend to move in circular paths thrive and flourish in the Garden of Eden. Thus two distinct species of microbes emerge as a result of natural selection.

 
