-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 24-07-2023 a las 00:56:05
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hospital`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cobro paciente`
--

CREATE TABLE `cobro paciente` (
  `id` int(100) NOT NULL,
  `Rut` varchar(100) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Prevision de salud` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Derivacion` varchar(100) NOT NULL,
  `Dias` int(100) NOT NULL,
  `Cobro` int(100) NOT NULL,
  `Descuento` int(100) NOT NULL,
  `Cobro total` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cobro paciente`
--

INSERT INTO `cobro paciente` (`id`, `Rut`, `Nombre`, `Prevision de salud`, `Derivacion`, `Dias`, `Cobro`, `Descuento`, `Cobro total`) VALUES
(5, '30.000.000-0', 'Penelope', 'Fonasa', 'Consulta medica', 2, 70000, 17500, 52500),
(6, '30.111.111-1', 'Caleb', 'Isapre', 'Urgencia', 4, 35000, 7000, 28000),
(7, '30.222.222-2', 'Madeline', 'Fonasa', 'Urgencia', 4, 35000, 8750, 26250),
(8, '30.333.333-3', 'Wyatt', 'Isapre', 'Consulta medica', 2, 70000, 14000, 56000),
(9, '30.444.444-4', 'Violeta', 'Fonasa', 'Consulta medica', 2, 70000, 17500, 52500),
(10, '30.555.555-5', 'Leo', 'Fonasa', 'Urgencia', 4, 35000, 8750, 26250),
(11, '30.666.666-6', 'Christopher', 'Particular', 'Consulta medica', 0, 20000, 0, 20000),
(12, '30.777.777-7', 'Aurora', 'Fonasa', 'Urgencia', 4, 35000, 8750, 26250),
(13, '30.888.888-8', 'Hannah', 'Isapre', 'Consulta medica', 0, 20000, 4000, 16000),
(14, '30.999.999-9', 'Matthew', 'Fonasa', 'Consulta medica', 2, 70000, 17500, 52500),
(15, '31.111.111-1', 'David', 'Isapre', 'Urgencia', 4, 35000, 7000, 28000),
(18, '31.222.222-2', 'Sergio', 'Particular', 'Consulta medica', 2, 70000, 0, 70000),
(19, '31.333.333-3', 'Hugo', 'Fonasa', 'Consulta medica', 3, 95000, 23750, 71250);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medico`
--

CREATE TABLE `medico` (
  `id` int(11) NOT NULL,
  `Rut` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha de ingreso` varchar(50) NOT NULL,
  `Prevision de salud` varchar(100) NOT NULL,
  `Sueldo bruto` int(100) NOT NULL,
  `Especialidad` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medico`
--

INSERT INTO `medico` (`id`, `Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Especialidad`) VALUES
(16, '1.111.111-1', 'Sofia', '1990-07-01', 'Fonasa', 1000000, 'Pediatria'),
(32, '1.222.222-2', 'Ethan', '1998-09-23', 'Isapre', 2500000, 'Gastroenterologia'),
(33, '1.333.333-3', 'Liam', '1990-05-23', 'Fonasa', 2000000, 'Cardiologia'),
(34, '1.444.444-4', 'Ava', '2000-08-23', 'Isapre', 1500000, 'Anestesiologia'),
(35, '1.555.555-5', 'Noah', '2005-10-26', 'Fonasa', 1800000, 'Pediatria'),
(37, '1.666.666-6', 'Fernando', '1997-07-18', 'Particular', 1500000, 'Obstetricia'),
(38, '1.777.777-7', 'Vicente', '1990-07-03', 'Fonasa', 2500000, 'Medicina General'),
(31, '10.000.000-0', 'Olivia', '2003-07-24', 'Fonasa', 1700000, 'Medicina General'),
(17, '2.222.222-2', 'Mateo', '1990-12-02', 'Isapre', 2000000, 'Anestesiologia'),
(18, '3.333.333-3', 'Valentina', '2000-02-14', 'Particular', 1200000, 'Cardiologia'),
(19, '4.444.444-4', 'Santiago', '2003-07-03', 'Fonasa', 2500000, 'Gastroenterologia'),
(20, '5.555.555-5', 'Isabella', '2005-12-12', 'Isapre', 1500000, 'Medicina General'),
(21, '6.666.666-6', 'Sebastian', '2010-12-24', 'Particular', 2000000, 'Ginecologia'),
(22, '7.777.777-7', 'Samuel de luque', '1990-07-03', 'Fonasa', 3000000, 'Obstetricia'),
(23, '8.888.888-8', 'Claudio', '2012-04-21', 'Fonasa', 1800000, 'Obstetricia'),
(24, '9.999.999-9', 'Daniel', '1990-07-03', 'Isapre', 2000000, 'Ginecologia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int(11) NOT NULL,
  `Rut` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha de ingreso` varchar(50) NOT NULL,
  `Prevision de salud` varchar(100) NOT NULL,
  `Motivo de ingreso` varchar(100) NOT NULL,
  `Derivacion` varchar(100) NOT NULL,
  `Medico atencion` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Box` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Motivo de ingreso`, `Derivacion`, `Medico atencion`, `Box`) VALUES
(40, '30.000.000-0', 'Penelope', '2023-07-18', 'Fonasa', 'Desmayo', 'Consulta medica', 'Liam Cardiologia', 0),
(41, '30.111.111-1', 'Caleb', '2023-07-18', 'Isapre', 'Accidente', 'Urgencia', 'N/A', 0),
(42, '30.222.222-2', 'Madeline', '2023-07-18', 'Fonasa', 'Parto', 'Urgencia', 'N/A', 1),
(43, '30.333.333-3', 'Wyatt', '2023-07-18', 'Isapre', 'Quemadura', 'Consulta medica', '{Samuel de luque} Obstetricia', 0),
(44, '30.444.444-4', 'Violeta', '2023-07-18', 'Fonasa', 'Vómito', 'Consulta medica', 'Sofia Pediatria', 0),
(45, '30.555.555-5', 'Leo', '2023-07-18', 'Fonasa', 'Hemorragia', 'Urgencia', 'N/A', 1),
(46, '30.666.666-6', 'Christopher', '2023-07-18', 'Particular', 'Infarto', 'Consulta medica', 'Liam Cardiologia', 0),
(47, '30.777.777-7', 'Aurora', '2023-07-18', 'Fonasa', 'Infección', 'Urgencia', 'N/A', 1),
(48, '30.888.888-8', 'Hannah', '2023-07-18', 'Isapre', 'Fiebre', 'Consulta medica', 'Noah Pediatria', 0),
(49, '30.999.999-9', 'Matthew', '2023-07-18', 'Fonasa', 'Apéndice', 'Consulta medica', 'Ethan Gastroenterologia', 0),
(50, '31.111.111-1', 'David', '2023-07-18', 'Isapre', 'Infarto', 'Urgencia', 'N/A', 1),
(53, '31.222.222-2', 'Sergio', '2023-07-20', 'Particular', 'Fractura', 'Consulta medica', 'Olivia {Medicina General}', 0),
(54, '31.333.333-3', 'Hugo', '2023-07-20', 'Fonasa', 'Infección', 'Consulta medica', 'Isabella {Medicina General}', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago personal`
--

CREATE TABLE `pago personal` (
  `id` int(11) NOT NULL,
  `Rut` varchar(100) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Sueldo bruto` int(100) NOT NULL,
  `Cargo` varchar(100) NOT NULL,
  `Descuentos` int(100) NOT NULL,
  `Bonificaciones` int(100) NOT NULL,
  `Sueldo liquido` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pago personal`
--

INSERT INTO `pago personal` (`id`, `Rut`, `Nombre`, `Sueldo bruto`, `Cargo`, `Descuentos`, `Bonificaciones`, `Sueldo liquido`) VALUES
(8, '1.111.111-1', 'Sofia', 1000000, 'Medico', 170000, 170000, 1000000),
(9, '2.222.222-2', 'Mateo\r\n', 2000000, 'Medico', 340000, 340000, 2000000),
(10, '3.333.333-3', 'Valentina\r\n', 1200000, 'Medico', 204000, 120000, 1116000),
(11, '4.444.444-4', 'Santiago \r\n', 2500000, 'Medico', 425000, 250000, 2325000),
(12, '5.555.555-5', 'Isabella \r\n', 1500000, 'Medico', 255000, 75000, 1320000),
(13, '6.666.666-6', 'Sebastian \r\n', 2000000, 'Medico', 340000, 100000, 1760000),
(14, '7.777.777-7', 'Samuel de luque', 3000000, 'Medico', 510000, 510000, 3000000),
(15, '8.888.888-8', 'Camila \r\n', 1800000, 'Medico', 306000, 90000, 1584000),
(16, '9.999.999-9', 'Daniel\r\n', 2000000, 'Medico', 340000, 340000, 2000000),
(23, '10.000.000-0', 'Olivia', 1700000, 'Medico', 289000, 85000, 1496000),
(24, '1.222.222-2', 'Ethan', 2500000, 'Medico', 425000, 250000, 2325000),
(25, '1.333.333-3', 'Liam', 2000000, 'Medico', 340000, 340000, 2000000),
(26, '1.444.444-4', 'Ava', 1500000, 'Medico', 255000, 150000, 1395000),
(27, '1.555.555-5', 'Noah\n', 1800000, 'Medico', 306000, 90000, 1584000),
(28, '10.111.111-1', 'Sophia', 1200000, 'Tens', 204000, 60000, 1056000),
(29, '10.222.222-2', 'Lucas', 1000000, 'Tens', 170000, 50000, 880000),
(30, '10.333.333-3', 'Mia', 1300000, 'Tens', 221000, 65000, 1144000),
(31, '10.444.444-4', 'Mason', 1400000, 'Tens', 238000, 70000, 1232000),
(32, '10.555.555-5', 'Amelia', 1800000, 'Tens', 306000, 306000, 1800000),
(33, '10.666.666-6', 'Logan', 1450000, 'Tens', 246500, 145000, 1348500),
(34, '10.777.777-7', 'Harper', 1250000, 'Tens', 212500, 125000, 1162500),
(35, '10.888.888-8', 'Oliver', 1200000, 'Tens', 204000, 60000, 1056000),
(36, '10.999.999-9', 'Evelyn', 1400000, 'Tens', 238000, 70000, 1232000),
(37, '11.111.111-1', 'Elijah', 1350000, 'Tens', 229500, 67500, 1188000),
(38, '11.222.222-2', 'Abigail', 1000000, 'Tens', 170000, 50000, 880000),
(39, '11.333.333-3', 'Aiden', 800000, 'Tens', 136000, 40000, 704000),
(40, '20.000.000-0', 'Emily', 2500000, 'Administrativo', 425000, 375000, 2450000),
(41, '20.111.111-1', 'Carter', 1800000, 'Administrativo', 306000, 54000, 1548000),
(42, '20.222.222-2', 'Scarlett', 1250000, 'Administrativo', 212500, 37500, 1075000),
(43, '20.333.333-3', 'Alexander', 800000, 'Administrativo', 136000, 24000, 688000),
(44, '20.444.444-4', 'Elizabeth\n', 700000, 'Administrativo', 119000, 21000, 602000),
(45, '20.555.555-5', 'James\n', 2500000, 'Administrativo', 425000, 375000, 2450000),
(46, '20.666.666-6', 'Benjamin', 1250000, 'Administrativo', 212500, 37500, 1075000),
(47, '20.777.888-8', 'Grace', 1000000, 'Administrativo', 170000, 30000, 860000),
(48, '20.888.888-8', 'William', 750000, 'Administrativo', 127500, 22500, 645000),
(49, '20.999.999-9', 'Chloe', 650000, 'Administrativo', 110500, 19500, 559000),
(51, '21.111.111-1', 'Henry', 2500000, 'Administrativo', 425000, 75000, 2150000),
(52, '21.222.222-2', 'Natalie', 1250000, 'Administrativo', 212500, 37500, 1075000),
(53, '21.333.333-3', 'Lila', 1000000, 'Administrativo', 170000, 30000, 860000),
(54, '21.444.444-4', 'Gabriel', 850000, 'Administrativo', 144500, 25500, 731000),
(55, '21.555.555-5', 'Alexander', 750000, 'Administrativo', 127500, 22500, 645000),
(56, '11.444.444-4', 'Matias', 1350000, 'Tens', 229500, 135000, 1255500),
(57, '21.666.666-6', 'Carlos', 800000, 'Administrativo', 136000, 24000, 688000),
(58, '1.666.666-6', 'Fernando', 1500000, 'Medico', 255000, 150000, 1395000),
(59, '11.555.555-5', 'Camila', 1100000, 'Tens', 187000, 55000, 968000),
(60, '21.777.777-7', 'Sofia', 1800000, 'Administrativo', 306000, 144000, 1638000),
(61, '1.777.777-7', 'Vicente', 2500000, 'Medico', 425000, 425000, 2500000),
(62, '11.666.666-6', 'Paola', 1700000, 'Tens', 289000, 170000, 1581000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal administrativo`
--

CREATE TABLE `personal administrativo` (
  `id` int(11) NOT NULL,
  `Rut` varchar(100) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha de ingreso` varchar(100) NOT NULL,
  `Prevision de salud` varchar(100) NOT NULL,
  `Sueldo bruto` varchar(100) NOT NULL,
  `Unidad administrativa` varchar(100) NOT NULL,
  `Cargo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personal administrativo`
--

INSERT INTO `personal administrativo` (`id`, `Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Unidad administrativa`, `Cargo`) VALUES
(8, '20.000.000-0', 'Emily', '1989-09-13', 'Fonasa', '2500000', 'Unidad de servicios generales', 'Jefe'),
(9, '20.111.111-1', 'Carter', '2004-09-16', 'Isapre', '1800000', 'Unidad de servicios generales', 'Secretario'),
(10, '20.222.222-2', 'Scarlett', '2011-01-11', 'Fonasa', '1250000', 'Unidad de servicios generales', 'Tesorero'),
(11, '20.333.333-3', 'Alexander', '2017-05-17', 'Isapre', '800000', 'Unidad de servicios generales', 'Asistente'),
(12, '20.444.444-4', 'Elizabeth\n', '2019-05-08', 'Fonasa', '700000', 'Unidad de servicios generales', 'Sin cargo'),
(13, '20.555.555-5', 'James\n', '1988-10-18', 'Isapre', '2500000', 'Unidad de personal', 'Jefe'),
(14, '20.666.666-6', 'Benjamin', '2010-01-05', 'Fonasa', '1250000', 'Unidad de personal', 'Secretario'),
(15, '20.777.888-8', 'Grace', '2010-01-05', 'Isapre', '1000000', 'Unidad de personal', 'Tesorero'),
(16, '20.888.888-8', 'William', '2017-05-17', 'Fonasa', '750000', 'Unidad de personal', 'Asistente'),
(17, '20.999.999-9', 'Chloe', '2017-05-17', 'Fonasa', '650000', 'Unidad de personal', 'Sin cargo'),
(18, '21.111.111-1', 'Henry', '2011-10-12', 'Fonasa', '2500000', 'Unidad de jefatura', 'Jefe'),
(19, '21.222.222-2', 'Natalie', '2006-12-12', 'Isapre', '1250000', 'Unidad de jefatura', 'Secretario'),
(20, '21.333.333-3', 'Lila', '2015-09-15', 'Fonasa', '1000000', 'Unidad de jefatura', 'Tesorero'),
(21, '21.444.444-4', 'Gabriel', '2019-05-06', 'Fonasa', '850000', 'Unidad de jefatura', 'Asistente'),
(22, '21.555.555-5', 'Alexander', '2022-07-12', 'Fonasa', '750000', 'Unidad de jefatura', 'Sin cargo'),
(23, '21.666.666-6', 'Carlos', '2015-09-15', 'Particular', '800000', 'Unidad de personal', 'Sin cargo'),
(24, '21.777.777-7', 'Sofia', '2000-07-31', 'Particular', '1800000', 'Unidad de jefatura', 'Tesorero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tens`
--

CREATE TABLE `tens` (
  `id` int(11) NOT NULL,
  `Rut` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha de ingreso` date NOT NULL,
  `Prevision de salud` varchar(100) NOT NULL,
  `Sueldo bruto` int(100) NOT NULL,
  `Area` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tens`
--

INSERT INTO `tens` (`id`, `Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Area`) VALUES
(5, '10.111.111-1', 'Sophia', '2009-07-23', 'Fonasa', 1200000, 'Consulta externa'),
(6, '10.222.222-2', 'Lucas', '2013-07-25', 'Isapre', 1000000, 'Emergencia'),
(7, '10.333.333-3', 'Mia', '2016-07-13', 'Fonasa', 1300000, 'Pediatria'),
(8, '10.444.444-4', 'Mason', '2018-07-17', 'Fonasa', 1400000, 'Quirofano'),
(9, '10.555.555-5', 'Amelia', '1990-10-11', 'Fonasa', 1800000, 'Hospitalizacion'),
(10, '10.666.666-6', 'Logan', '1995-12-20', 'Isapre', 1450000, 'Recuperacion UCI'),
(11, '10.777.777-7', 'Harper', '2000-01-01', 'Fonasa', 1250000, 'Recuperacion UCI'),
(12, '10.888.888-8', 'Oliver', '2010-06-16', 'Isapre', 1200000, 'Hospitalizacion'),
(13, '10.999.999-9', 'Evelyn', '2015-03-18', 'Fonasa', 1400000, 'Quirofano'),
(14, '11.111.111-1', 'Elijah', '2018-03-20', 'Isapre', 1350000, 'Pediatria'),
(15, '11.222.222-2', 'Abigail', '2021-09-17', 'Isapre', 1000000, 'Emergencia'),
(16, '11.333.333-3', 'Aiden', '2023-07-17', 'Fonasa', 800000, 'Consulta externa'),
(17, '11.444.444-4', 'Matias', '2000-09-18', 'Particular', 1350000, 'Pediatria'),
(18, '11.555.555-5', 'Camila', '2020-08-05', 'Particular', 1100000, 'Quirofano'),
(19, '11.666.666-6', 'Paola', '1996-09-20', 'Isapre', 1700000, 'Recuperacion UCI');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cobro paciente`
--
ALTER TABLE `cobro paciente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`Rut`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`Rut`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `pago personal`
--
ALTER TABLE `pago personal`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `personal administrativo`
--
ALTER TABLE `personal administrativo`
  ADD PRIMARY KEY (`Rut`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `tens`
--
ALTER TABLE `tens`
  ADD PRIMARY KEY (`Rut`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cobro paciente`
--
ALTER TABLE `cobro paciente`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `medico`
--
ALTER TABLE `medico`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT de la tabla `pago personal`
--
ALTER TABLE `pago personal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de la tabla `personal administrativo`
--
ALTER TABLE `personal administrativo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `tens`
--
ALTER TABLE `tens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
