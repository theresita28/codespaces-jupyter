import java.util.Scanner;

public class GültigkeitDatum {
  
   public static boolean proofDate(double tag, double monatx, double jahr) {
       boolean proofDate = false;
       long monaty = Math.round(monatx);
       int monat = (int) monaty;
       
        if ( monat < 13) {
           if ( jahr > 0){
             switch (monat) {
               case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                 if( tag <= 31) {
                  proofDate = true;
                 } 
                 else{
                  proofDate = false;
                 }
                  break;
               case 4: case 6: case 9: case 11:
                 if( tag <= 30) {
                  proofDate = true;
                 } 
                 else{
                  proofDate = false;
                 }
                  break;
               case 2:
                 if( tag <= 28) {
                  proofDate = true;
                 } 
                 else{
                  proofDate = false;
                 }
                  break;
               
             }
            }
            else{
               proofDate = false;
            }
          
        }
        else{
         proofDate = false;
        } // end of if 

      return proofDate;
     }
    public static void main(String[] args) {
        double tag, monat, jahr;
        Scanner scanner = new Scanner(System.in);
    
        System.out.println("Datum zum Prüfen");
        System.out.println("Tag: ");
        tag = scanner.nextDouble();
        
       System.out.println("Monat: ");
       monat = scanner.nextDouble();
      
       System.out.println("Jahr: ");
       jahr = scanner.nextByte();

       System.out.println("Das Datum is " + proofDate(tag, monat, jahr));
       scanner.close();
    }
}