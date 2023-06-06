import 'package:control_panel/pages/home.dart';
import 'package:flutter/material.dart';
//import 'package:control_panel/pages/auth.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Travelers Control Panel',
      debugShowCheckedModeBanner: false,
      home: HomePage(),//LoginPage(),
    );
  }
}