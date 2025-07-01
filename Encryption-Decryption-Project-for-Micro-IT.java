import javax.swing.*;
public class EncryptionDecryptionTool{
    static final String PLAIN = "abcdefghijklmnopqrstuvwxyz";
    static final String CIPHER = "cdefghijklmnopqrstuvwxyzab";
    public static void main(String[] args) {
        String[] options = {"Encrypt", "Decrypt"};
        int choice = JOptionPane.showOptionDialog(
                null,
                "Choose an option",
                "Cipher Tool",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.INFORMATION_MESSAGE,
                null,
                options,
                options[0]
        );
        if (choice == JOptionPane.CLOSED_OPTION) {
            return; // User closed the dialog
        }
        String input = JOptionPane.showInputDialog(null, "Enter the text:", "Input", JOptionPane.PLAIN_MESSAGE);
        if (input == null) {
            return; // User cancelled input
        }
        input = input.toLowerCase();
        String result;

        if (choice == 0) {
            result = encrypt(input);
        } else {
            result = decrypt(input);
        }
        JOptionPane.showMessageDialog(null, result, "Result", JOptionPane.INFORMATION_MESSAGE);
    }
    public static String encrypt(String text) {
        StringBuilder encrypted = new StringBuilder();
        for (char ch : text.toCharArray()) {
            int index = PLAIN.indexOf(ch);
            encrypted.append(index != -1 ? CIPHER.charAt(index) : ch);
        }
        return encrypted.toString();
    }
    public static String decrypt(String text) {
        StringBuilder decrypted = new StringBuilder();
        for (char ch : text.toCharArray()) {
            int index = CIPHER.indexOf(ch);
            decrypted.append(index != -1 ? PLAIN.charAt(index) : ch);
        }
        return decrypted.toString();
    }
}