using System;

namespace DesignPatterns.Mediator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Створюємо два злітно-посадкові смуги
            Runway runway1 = new Runway();
            Runway runway2 = new Runway();

            // Створюємо літаки
            Aircraft aircraft1 = new Aircraft("Boeing");
            Aircraft aircraft2 = new Aircraft("Airbus");

            // Створюємо центр управління
            CommandCentre commandCentre = new CommandCentre(new Runway[] { runway1, runway2 }, new Aircraft[] { aircraft1, aircraft2 });

            // Літак 1: запит на посадку на першій смузі
            commandCentre.RequestToLand(aircraft1, runway1);

            // Літак 2: запит на взліт з другої смуги
            commandCentre.RequestToTakeOff(aircraft2, runway2);

            // Літак 1: запит на взліт, але смуга ще зайнята
            commandCentre.RequestToTakeOff(aircraft1, runway1);
        }
    }
}
