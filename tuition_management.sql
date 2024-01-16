-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 07:09 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tuition_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_information`
--

CREATE TABLE `student_information` (
  `student_name` varchar(30) NOT NULL,
  `student_id` bigint(10) NOT NULL,
  `phone_number` bigint(10) NOT NULL,
  `student_email` varchar(20) NOT NULL,
  `student_password` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_information`
--

INSERT INTO `student_information` (`student_name`, `student_id`, `phone_number`, `student_email`, `student_password`) VALUES
('raziq ', 2022431, 122096690, 'raziq20@gmail.com', '167827'),
('sara ', 2022786, 106632756, 'sara.m@gmail.com', '56724'),
('zaza', 2022917, 162522685, 'zaza167@gmail.com', '24267'),
('kamaruddin ', 2022691, 195724189, 'din675@gmail.com', '13279');

-- --------------------------------------------------------

--
-- Table structure for table `subject_information`
--

CREATE TABLE `subject_information` (
  `stu_name` char(100) NOT NULL,
  `stu_id` varchar(10) NOT NULL,
  `sub_package` varchar(10) NOT NULL,
  `total_price` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subject_information`
--

INSERT INTO `subject_information` (`stu_name`, `stu_id`, `sub_package`, `total_price`) VALUES
('yaya', '202234567', 'Package 1', '508.0'),
('azim', '202298765', 'Package 1', '508.0'),
('abdul razak', '202245679', 'Package 5', '528.0'),
('fatihah', '20220171', 'Package 2', '508.0'),
('athirah', '2021884732', 'Package 5', '465.8'),
('najuwa', '2021904212', 'Package 3', '518');

-- --------------------------------------------------------

--
-- Table structure for table `tuition_branches`
--

CREATE TABLE `tuition_branches` (
  `student_id` int(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `method` varchar(10) NOT NULL,
  `tui_area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tuition_branches`
--

INSERT INTO `tuition_branches` (`student_id`, `password`, `method`, `tui_area`) VALUES
(16782, '1427', 'Select You', 'Kedah : Kulim'),
(17195, '234567', 'online', 'ZOOM'),
(345678, '2349', 'face-to-fa', 'Selangor : Shah Alam'),
(5678, '1027', 'face-to-fa', 'Johor : Muar '),
(222890, '8167', 'face-to-fa', 'Selangor : Sepang'),
(23456789, '4567098', 'online', 'WEBEX');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
