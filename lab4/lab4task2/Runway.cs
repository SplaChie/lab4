using System;

namespace DesignPatterns.Mediator
{
    class Runway
    {
        public readonly Guid Id = Guid.NewGuid();
        private Aircraft _aircraft;

        public bool IsAvailable()
        {
            return _aircraft == null;
        }

        public bool CheckIsActive()
        {
            return _aircraft != null && _aircraft.IsTakingOff;
        }

        public void AssignRunway(Aircraft aircraft)
        {
            _aircraft = aircraft;
        }

        public void HighLightRed()
        {
            Console.WriteLine($"Runway {Id} is busy!");
        }

        public void HighLightGreen()
        {
            Console.WriteLine($"Runway {Id} is free!");
            _aircraft = null;
        }
    }
}
