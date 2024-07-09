using System;

namespace DesignPatterns.Mediator
{
    class Aircraft
    {
        public string Name { get; private set; }
        public bool IsTakingOff { get; private set; }

        public Aircraft(string name)
        {
            Name = name;
        }

        public void Land(Runway runway)
        {
            Console.WriteLine($"Aircraft {Name} is landing.");
            IsTakingOff = false;
            runway.HighLightRed();
        }

        public void TakeOff(Runway runway)
        {
            Console.WriteLine($"Aircraft {Name} is taking off.");
            IsTakingOff = true;
            runway.HighLightGreen();
        }
    }
}
