import 'package:flutter/material.dart';

void main() {
  runApp(const GBRApp());
}

class GBRApp extends StatelessWidget {
  const GBRApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GBR App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF6750A4),
          brightness: Brightness.light,
        ),
        useMaterial3: true,
        appBarTheme: const AppBarTheme(
          centerTitle: true,
          elevation: 0,
        ),
      ),
      home: const GBRHomePage(),
    );
  }
}

class GBRHomePage extends StatefulWidget {
  const GBRHomePage({super.key});

  @override
  State<GBRHomePage> createState() => _GBRHomePageState();
}

class _GBRHomePageState extends State<GBRHomePage>
    with TickerProviderStateMixin {
  late TabController _tabController;
  int _selectedIndex = 0;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'GBR App',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        backgroundColor: Theme.of(context).colorScheme.surface,
        foregroundColor: Theme.of(context).colorScheme.onSurface,
      ),
      body: Column(
        children: [
          Container(
            margin: const EdgeInsets.all(16),
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [
                  Theme.of(context).colorScheme.primary,
                  Theme.of(context).colorScheme.secondary,
                ],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(16),
            ),
            child: const Column(
              children: [
                Icon(
                  Icons.flutter_dash,
                  size: 48,
                  color: Colors.white,
                ),
                SizedBox(height: 16),
                Text(
                  'Добро пожаловать в GBR App!',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 8),
                Text(
                  'Flutter приложение с Java 21, Gradle 8.9 и Kotlin 2.1.0',
                  style: TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          ),
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: [
                _buildFeaturesTab(),
                _buildAboutTab(),
                _buildSettingsTab(),
              ],
            ),
          ),
        ],
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _selectedIndex,
        onDestinationSelected: (int index) {
          setState(() {
            _selectedIndex = index;
            _tabController.animateTo(index);
          });
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.star),
            label: 'Возможности',
          ),
          NavigationDestination(
            icon: Icon(Icons.info),
            label: 'О приложении',
          ),
          NavigationDestination(
            icon: Icon(Icons.settings),
            label: 'Настройки',
          ),
        ],
      ),
    );
  }

  Widget _buildFeaturesTab() {
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        _buildFeatureCard(
          icon: Icons.android,
          title: 'Android Support',
          description: 'Полная поддержка Android с Java 21',
          color: Colors.green,
        ),
        _buildFeatureCard(
          icon: Icons.code,
          title: 'Kotlin 2.1.0',
          description: 'Современный Kotlin для разработки',
          color: Colors.orange,
        ),
        _buildFeatureCard(
          icon: Icons.build,
          title: 'Gradle 8.9',
          description: 'Мощная система сборки',
          color: Colors.blue,
        ),
        _buildFeatureCard(
          icon: Icons.flutter_dash,
          title: 'Flutter',
          description: 'Кроссплатформенная разработка',
          color: Colors.cyan,
        ),
      ],
    );
  }

  Widget _buildAboutTab() {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Технические характеристики',
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  const SizedBox(height: 16),
                  _buildInfoRow('Java Version', '21'),
                  _buildInfoRow('Gradle Version', '8.9'),
                  _buildInfoRow('Kotlin Version', '2.1.0'),
                  _buildInfoRow('Flutter Version', '3.9.0+'),
                  _buildInfoRow('Dart Version', '3.9.0+'),
                ],
              ),
            ),
          ),
          const SizedBox(height: 16),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Описание',
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  const SizedBox(height: 8),
                  const Text(
                    'GBR App - это современное Flutter приложение, демонстрирующее '
                    'использование последних версий технологий разработки. '
                    'Приложение построено с использованием Material Design 3 '
                    'и поддерживает все современные платформы.',
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSettingsTab() {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Настройки',
            style: Theme.of(context).textTheme.headlineSmall,
          ),
          const SizedBox(height: 16),
          SwitchListTile(
            title: const Text('Темная тема'),
            subtitle: const Text('Включить темную тему приложения'),
            value: false,
            onChanged: (value) {
              // TODO: Implement dark theme
            },
          ),
          SwitchListTile(
            title: const Text('Уведомления'),
            subtitle: const Text('Получать push-уведомления'),
            value: true,
            onChanged: (value) {
              // TODO: Implement notifications
            },
          ),
          SwitchListTile(
            title: const Text('Автообновление'),
            subtitle: const Text('Автоматически обновлять данные'),
            value: false,
            onChanged: (value) {
              // TODO: Implement auto-update
            },
          ),
        ],
      ),
    );
  }

  Widget _buildFeatureCard({
    required IconData icon,
    required String title,
    required String description,
    required Color color,
  }) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: color.withOpacity(0.1),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Icon(
                icon,
                color: color,
                size: 32,
              ),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: Theme.of(context).textTheme.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    description,
                    style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                      color: Theme.of(context).colorScheme.onSurfaceVariant,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            label,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
              color: Theme.of(context).colorScheme.onSurfaceVariant,
            ),
          ),
          Text(
            value,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
