namespace LogicalPattern
{
    internal class MainApp
    {
        static void Main(string[] args)
        {
            static string GetGrade(double score) => score switch
            {
                < 60 => "F",
                >= 60 and < 70 => "D",
                >= 70 and < 80 => "C",
                >= 80 and < 90 => "B",
                _ => "A",
            };

        }
    }
}