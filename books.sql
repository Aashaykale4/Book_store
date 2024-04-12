SELECT * FROM public.book
ORDER BY id ASC ;

INSERT INTO public.book (title, author, avg_rating, format, image, num_pages, pub_id) VALUES
('Miky''s Delivery Service', 'William Dobelli', 3.9, 'ePub', 'broom-145379.svg', 123, 1),
('The Secret Life of Walter Kitty', 'Kitty Stiller', 4.1, 'Hardcover', 'cat-150306.svg', 133, 1),
('The Empty Book of Life', 'Roy Williamson', 4.2, 'eBook', 'book-life-34063.svg', 153, 1),
('Life After Dealth', 'Nikita Kimmel', 3.8, 'Paperback', 'mummy-146868.svg', 175, 2),
('The Legend of Dracula', 'Charles Rowling', 4.6, 'Hardcover', 'man-37603.svg', 253, 2),
('Taming Dragons', 'James Vonnegut', 4.5, 'MassMarket Paperback', 'dragon-23164.svg', 229, 2),
('The Singing Magpie', 'Oscar Steinbeck', 5, 'Hardcover', 'magpie-147852.svg', 188, 3),
('Mr. Incognito', 'Amelia Funke', 4.2, 'Hardcover', 'incognito-160143.svg', 205, 3),
('A Dog without purpose', 'Edgar Dahl', 4.8, 'MassMarket Paperback', 'dog-159271.svg', 300, 4),
('A Frog''s Life', 'Herman Capote', 3.9, 'MassMarket Paperback', 'amphibian-150342.svg', 190, 4),
('Logan Returns', 'Margaret Elliot', 4.6, 'Hardcover', 'wolf-153648.svg', 279, 5),
('Thieves of Kaalapani', 'Mohit Gustav', 4.1, 'Paperback', 'boat-1296201.svg', 270, 5),
('As Men Thinketh', 'Edward McPhee', 4.5, 'Paperback', 'cranium-2028555.svg', 124, 6),
('Mathematics of Music', 'Mary Turing', 4.5, 'Hardcover', 'music-306008.svg', 120, 6),
('The Mystery of Mandalas', 'Jack Morrison', 4.2, 'Paperback', 'mandala-1817599.svg', 221, 6),
('The Sacred Book of Kairo', 'Heidi Zimmerman', 3.8, 'ePub', 'book-1294676.svg', 134, 7),
('Love is forever, As Long as it lasts', 'Kovi O''Hara', 4.5, 'Hardcover', 'love-2026554.svg', 279, 8),
('Order in Chaos', 'Wendy Sherman', 3.5, 'MassMarket Paperback', 'chaos-1769656.svg', 140, 8);
