# GBR App

Современное Flutter приложение, созданное с использованием последних версий технологий разработки.

## 🚀 Технические характеристики

- **Java**: 21
- **Gradle**: 8.9
- **Kotlin**: 2.1.0
- **Flutter**: 3.9.0+
- **Dart**: 3.9.0+

## 📋 Требования

### Системные требования
- Windows 10/11
- Flutter SDK 3.9.0 или выше
- Java Development Kit (JDK) 21
- Android Studio (рекомендуется)

### Установка Java 21
1. Скачайте JDK 21 с официального сайта Oracle или используйте OpenJDK
2. Установите JDK в папку `C:\Program Files\Java\jdk-21`
3. Добавьте `C:\Program Files\Java\jdk-21\bin` в переменную PATH

### Установка Flutter
1. Скачайте Flutter SDK с [flutter.dev](https://flutter.dev)
2. Распакуйте в папку (например, `C:\flutter`)
3. Добавьте `C:\flutter\bin` в переменную PATH
4. Запустите `flutter doctor` для проверки установки

## 🛠️ Настройка проекта

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd gbr_app
```

### 2. Установка зависимостей
```bash
flutter pub get
```

### 3. Проверка настроек
```bash
flutter doctor
```

### 4. Настройка Android
Убедитесь, что в `android/gradle.properties` указан правильный путь к Java:
```properties
org.gradle.java.home=C:\\Program Files\\Java\\jdk-21
```

## 🚀 Запуск приложения

### Запуск на Android устройстве/эмуляторе
```bash
flutter run
```

### Запуск в режиме отладки
```bash
flutter run --debug
```

### Сборка APK
```bash
flutter build apk
```

### Сборка App Bundle
```bash
flutter build appbundle
```

## 📱 Возможности приложения

- **Современный UI**: Material Design 3
- **Адаптивный дизайн**: Поддержка различных размеров экранов
- **Темы**: Светлая тема (темная тема в разработке)
- **Навигация**: Tab-based навигация с bottom navigation bar
- **Информация**: Детальная информация о технологиях проекта

## 🏗️ Структура проекта

```
gbr_app/
├── android/                 # Android-специфичные файлы
│   ├── app/                # Основное Android приложение
│   ├── gradle/             # Gradle wrapper
│   └── build.gradle.kts    # Основной Gradle файл
├── lib/                    # Dart код
│   └── main.dart          # Главный файл приложения
├── ios/                    # iOS-специфичные файлы
├── web/                    # Web-специфичные файлы
├── windows/                # Windows-специфичные файлы
├── linux/                  # Linux-специфичные файлы
├── macos/                  # macOS-специфичные файлы
└── pubspec.yaml            # Зависимости Flutter
```

## 🔧 Настройка Gradle

Проект использует Gradle 8.9 с Kotlin DSL. Основные настройки:

- **Gradle Wrapper**: 8.9
- **Kotlin Plugin**: 2.1.0
- **Java Compatibility**: 21
- **Android Plugin**: Последняя версия

## 📊 Мониторинг и отладка

### Flutter Inspector
Используйте Flutter Inspector в Android Studio или VS Code для отладки UI.

### DevTools
```bash
flutter run --debug
# Затем откройте DevTools в браузере
```

### Логи
```bash
flutter logs
```

## 🚨 Устранение неполадок

### Проблемы с Java
- Убедитесь, что JAVA_HOME указывает на JDK 21
- Проверьте, что `java -version` показывает версию 21

### Проблемы с Gradle
- Очистите кэш: `flutter clean`
- Удалите папку `.gradle` в android/
- Перезапустите IDE

### Проблемы с Flutter
- Запустите `flutter doctor` для диагностики
- Обновите Flutter: `flutter upgrade`

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для деталей.

## 📞 Поддержка

Если у вас есть вопросы или проблемы:
- Создайте Issue в репозитории
- Обратитесь к документации Flutter
- Проверьте Flutter Community

---

**GBR App** - Создано с ❤️ используя Flutter, Java 21, Gradle 8.9 и Kotlin 2.1.0
