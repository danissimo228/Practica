-- Mariadb dump


CREATE TABLE Notifications
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(8) NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    lastSentAt int
);

INSERT Notifications(type, title, content, lastSentAt) VALUES ('SUCCES', 'Hello', 'How are u?', UNIX_TIMESTAMP(NOW())),
        (' WARNING', 'Some text', 'not good', UNIX_TIMESTAMP(NOW())),
        (' FAIL', 'Very bad', 'bad text!', UNIX_TIMESTAMP(NOW()));