title: Fusor Build
date: 26-12-2019
---

## Why have a fusor? 

### Motivation for the build

A fusor, or Farnsworth Fusor, is a fusion device that uses the principles of
Inertial Electrostatic Confinement to achieve fusion. Essentially, a fuel gas is heated to very high temperatures and accelerated through a highly negatively charged grid, which eventually leads to Fusion into He3, or Helium, with a large energy release.

The fuel gas is usually deuterium, due to its relative stability, lack of radioactivity, and fuse-ability; a Tritium fuel has a much higher cross section and efficiency of fusion, but is radioactive, and much more expensive than deuterium, which can be drawn off of sea water if needed.

When used in concert with proper detection methods and learning devices, they are a great tool.
They is useful in physics for several reasons, but our motivations were the following:

  +  It was a good beginner engineering and applied physics project.
  +  It keeps our machining and electronics skills up. 
  +  Our school has no engineering department or useable machine shop, so this is something we can make external connections to machinists and professional scientists with. 
  +  It allows us to study fusion processes, particle scattering, and particle detections methods for relatively low cost; the total build over several months has a predicted cost of about $500.00, rather than the exorbitant professional cost of most hadron accelerators.
  +  It's fun!


## The Process 
### Our build progress 
​	The components that matter are widely available, but we (as of this writing, May 2019) chose tofollow a fusor build approach outlined in Make Magazine. In turn, we ran into some minor issues with the chamber glass and standoffs, so we are considering (after consulting Dr. Liam Duffy) moving to a chamber cut and welded from a propane tank or similar object. To achieve the necessary voltage drop, a variac or variable step-up transformer is used. We can't afford a true variac for our purposes, so we are building a 'scariac', or variac using an electrolyte solution (in this case lye) and a 'crank' or manual lever to step-up.

​	After much consideration, we decided to make the build compatible with either an Arduino or Raspberry Pi programmable controller, so that we could operate it without risk of vacuum chamber collapse or radiation damaging our persons. The problems raised by this are those of the neutrons: most of the output of this voltage, pressure, and fuel will be in the form of Thermal Neutrons. Neutrons are very damaging to electronics, so we will place a 'neturon-proof' casing around the scariac, controller, and  monitoring equipment. 
