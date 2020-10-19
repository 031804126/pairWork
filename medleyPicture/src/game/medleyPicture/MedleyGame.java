package game.medleyPicture;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import javax.swing.border.TitledBorder;

public class MedleyGame extends JFrame {
    private JLabel modelLabel;
    private JPanel centerPanel;
    private JButton emptyButton;
    int num = 0;
    int nums = 0;

    public static void main(String[] args) {
        try {
            MedleyGame frame = new MedleyGame();
            frame.setVisible(true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //建立窗口构造方法
    public MedleyGame() {
        super();
        System.out.println(111);
        setResizable(false);
        setTitle("拼图游戏");
        setBounds(100, 100, 370, 525);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //创建面板对象，并增加边框、布局
        final JPanel topPanel = new JPanel();
        topPanel.setBorder(new TitledBorder(null, "", TitledBorder.DEFAULT_JUSTIFICATION,
                TitledBorder.DEFAULT_POSITION, null, null));
        topPanel.setLayout(new BorderLayout());
        getContentPane().add(topPanel, BorderLayout.NORTH);//放于上方
        //创建标签放原图
        modelLabel = new JLabel();
        modelLabel.setIcon(new ImageIcon("image/" + num + "model.jpg"));
        topPanel.add(modelLabel, BorderLayout.WEST);
        //在右侧加个面板，添加两个按钮
        JPanel eastPanel = new JPanel();
        topPanel.add(eastPanel, BorderLayout.CENTER);
        eastPanel.setLayout(new BorderLayout());
        JButton nextButton = new JButton();
        nextButton.setText("下一张");
        nextButton.addActionListener(new NextButtonAction());
        eastPanel.add(nextButton, BorderLayout.NORTH);
        //创建按钮开局添加监听
        final JButton startButton = new JButton();
        startButton.setText("开局");
        startButton.addActionListener(new StartButtonAction());
        eastPanel.add(startButton, BorderLayout.CENTER);
        //初始化中心面板，设置边框，添加按钮
        centerPanel = new JPanel();
        centerPanel.setBorder(new TitledBorder(null, "", TitledBorder.DEFAULT_JUSTIFICATION,
                TitledBorder.DEFAULT_POSITION, null, null));
        centerPanel.setLayout(new GridLayout(4, 0));
        getContentPane().add(centerPanel, BorderLayout.CENTER);
        //初始化图片
        String[][] exactnessOrder = order();
        //按排列添加按钮，设置图片
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                final JButton button = new JButton();
                button.setName(row + "" + col);
                button.setIcon(new ImageIcon(exactnessOrder[row][col]));
                if (exactnessOrder[row][col].equals("image/" + num + "00.jpg"))
                    emptyButton = button;
                button.addActionListener(new ImgButtonAction());
                centerPanel.add(button);
            }
        }
    }

    //初始化图片
    private String[][] order() {
        System.out.println(222);
        String[][] exactnessOrder = new String[4][4];
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                exactnessOrder[row][col] = "image/" + num + row + col + ".jpg";
            }
        }
        return exactnessOrder;
    }

    //随机排列图片
    private String[][] reorder() {
        System.out.println(333);
        String[][] exactnessOrder = new String[4][4];
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                exactnessOrder[row][col] = "image/" + num + row + col + ".jpg";
            }
        }
        String[][] stochasticOrder = new String[4][4];
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                while (stochasticOrder[row][col] == null) {
                    int r = (int) (Math.random() * 4);
                    int c = (int) (Math.random() * 4);
                    if (exactnessOrder[r][c] != null) {
                        stochasticOrder[row][col] = exactnessOrder[r][c];
                        exactnessOrder[r][c] = null;
                    }
                }
            }
        }
        return stochasticOrder;
    }

    //游戏时排列图片
    class ImgButtonAction implements ActionListener {
        public void actionPerformed(ActionEvent e) {
//			System.out.println(444);
            nums++;
//			System.out.println(nums);
            if (nums > 20) {
                JButton clickButton = (JButton) e.getSource();
                JPanel panel = (JPanel) clickButton.getParent();
                JButton one;
                while ((one = (JButton) panel.getComponent((int) (Math.random() * panel.getComponentCount()))) == emptyButton) {
                }
                JButton two;
                while ((two = (JButton) panel.getComponent((int) (Math.random() * panel.getComponentCount()))) == emptyButton || two == one) {
                }
                Icon icon=one.getIcon();
                one.setIcon(two.getIcon());
                two.setIcon(icon);
                nums=0;
            } else {
                String emptyName = emptyButton.getName();
                char emptyRow = emptyName.charAt(0);
//			System.out.println(emptyRow);
                if (emptyRow == '1') {
                    System.out.println("s");
                } else {
                    System.out.println("w");
                }

                char emptyCol = emptyName.charAt(1);
//			System.out.println(emptyCol);
                JButton clickButton = (JButton) e.getSource();
                String clickName = clickButton.getName();
                char clickRow = clickName.charAt(0);
                if (emptyRow == '1') {
                    System.out.println("a");
                } else {
                    System.out.println("d");
                }
//			System.out.println(clickRow);
                char clickCol = clickName.charAt(1);
//			System.out.println(clickCol);
                if (Math.abs(clickRow - emptyRow) + Math.abs(clickCol - emptyCol) == 1) {
                    emptyButton.setIcon(clickButton.getIcon());
                    clickButton.setIcon(new ImageIcon("image/" + num + "00.jpg"));
                    emptyButton = clickButton;
                }
            }
        }
    }

    //换下一张图片
    class NextButtonAction implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println(555);
            if (num == 5) {
                num = 0;
            } else {
                ++num;
            }
            modelLabel.setIcon(new ImageIcon("image/" + num + "model.jpg"));
            String[][] exactnessOrder = order();
            int i = 0;
            for (int row = 0; row < 4; row++) {
                for (int col = 0; col < 4; col++) {
                    JButton button = (JButton) centerPanel.getComponent(i++);
                    button.setIcon(new ImageIcon(exactnessOrder[row][col]));
                    if (exactnessOrder[row][col].equals("image/" + num + "00.jpg"))
                        emptyButton = button;
                }
            }
        }
    }

    //开局排列图片
    class StartButtonAction implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            System.out.println(666);
            String[][] stochasticOrder = reorder();
            int i = 0;
            for (int row = 0; row < 4; row++) {
                for (int col = 0; col < 4; col++) {
                    JButton button = (JButton) centerPanel.getComponent(i++);
                    button.setIcon(new ImageIcon(stochasticOrder[row][col]));
                    if (stochasticOrder[row][col].equals("image/" + num + "00.jpg"))
                        emptyButton = button;
                }
            }
        }
    }
}