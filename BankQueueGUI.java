import javax.swing.*;
import java.awt.*;
import java.util.LinkedList;

class Nasabah {
    int nomor;
    String nama;

    Nasabah(int nomor, String nama) {
        this.nomor = nomor;
        this.nama = nama;
    }
    @Override
    public String toString() { return nomor + ". " + nama; }
}

public class BankQueueGUI extends JFrame {
    private LinkedList<Nasabah> queue = new LinkedList<>();
    private int counter = 0;
    
    private JTextField txtNama = new JTextField(15);
    private DefaultListModel<String> listModel = new DefaultListModel<>();
    private JList<String> listAntrian = new JList<>(listModel);

    public BankQueueGUI() {
        setTitle("Simulasi Antrian Bank - Java");
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        add(new JLabel("Nama Nasabah:"));
        add(txtNama);

        JButton btnAmbil = new JButton("Ambil Antrian");
        JButton btnPanggil = new JButton("Panggil Antrian");

        add(btnAmbil);
        add(btnPanggil);
        add(new JScrollPane(listAntrian));
        listAntrian.setPreferredSize(new Dimension(300, 300));

        btnAmbil.addActionListener(e -> {
            String nama = txtNama.getText();
            if (!nama.isEmpty()) {
                counter++;
                Nasabah n = new Nasabah(counter, nama);
                queue.addLast(n);
                listModel.addElement(n.toString());
                txtNama.setText("");
                JOptionPane.showMessageDialog(this, "Nomor Antrian: " + counter);
            }
        });

        btnPanggil.addActionListener(e -> {
            if (!queue.isEmpty()) {
                Nasabah n = queue.removeFirst();
                listModel.remove(0);
                String msg = "Nomor antrian " + n.nomor + ", " + n.nama + ", ke loket.";
                speak(msg);
                JOptionPane.showMessageDialog(this, msg);
            } else {
                JOptionPane.showMessageDialog(this, "Antrian Kosong!");
            }
        });
    }

    // Fungsi suara menggunakan PowerShell (Windows Only)
    private void speak(String text) {
        try {
            String command = "Add-Type -AssemblyName System.Speech; " +
                             "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; " +
                             "$speak.Speak('" + text + "')";
            new ProcessBuilder("powershell", "-Command", command).start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new BankQueueGUI().setVisible(true));
    }
}