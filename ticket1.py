from abc import ABC, abstractmethod
import librosa
import sounddevice as sd

data, sr = librosa.load("../data/ml_1.mp3", sr=None)
# ==================== Интерфейс Mob ====================
class Mob(ABC):
    @abstractmethod
    def display(self) -> str:
        """Отобразить моба"""
        pass
    
    @abstractmethod
    def attack(self) -> str:
        """Выполнить атаку"""
        pass
    
    @abstractmethod
    def make_sound(self) -> str:
        """Издать характерный звук"""
        pass


# ==================== Конкретные классы мобов ====================
class Creeper(Mob):
    def __init__(self):
        self.name = "Крипер"
    
    def display(self) -> str:
        return f"[{self.name}] Зеленое существо с четырьмя ногами, шипит"
    
    def attack(self) -> str:
        return f"{self.name}: Начинает шипеть и взрывается через 1.5 секунды!"
    
    def make_sound(self) -> str:
        return "Тсссс... (шипение перед взрывом)"


class Skeleton(Mob):
    def __init__(self):
        self.name = "Скелет"
    
    def display(self) -> str:
        return f"[{self.name}] Костяной лучник с луком и стрелами"
    
    def attack(self) -> str:
        return f"{self.name}: Стреляет стрелой из лука!"
    
    def make_sound(self) -> str:
        return "*скрежет костей* ... Клац-клац!"


class Mellstroy(Mob):
    def __init__(self, biome_type: str = ""):
        self.name = "Мелстрой"
        self.biome_type = biome_type
    
    def display(self) -> str:
        biome_info = f" из биома {self.biome_type}" if self.biome_type else ""
        return f"[{self.name}{biome_info}] Мирный моб, который любит казино"
    
    def attack(self) -> str:
        return f"{self.name}: Я уже красный, культурно не получится"
    
    def make_sound(self) -> str:
        sd.play(data, sr)
        sd.wait()
        return "Быстрее! Быстрее! "
        
      


# ==================== Абстрактная фабрика ====================
class MobFactory(ABC):
    @abstractmethod
    def create_hostile_mob(self) -> Mob:
        """Создать враждебного моба"""
        pass
    
    @abstractmethod
    def create_neutral_mob(self) -> Mob:
        """Создать нейтрального моба"""
        pass


# ==================== Конкретные фабрики для биомов ====================
class ForestMobFactory(MobFactory):
    """Фабрика для лесного биома"""
    
    def create_hostile_mob(self) -> Mob:
        return Skeleton()
    
    def create_neutral_mob(self) -> Mob:
        return Mellstroy("Лес")


class MeadowMobFactory(MobFactory):
    """Фабрика для биома поляны"""
    
    def create_hostile_mob(self) -> Mob:
        return Creeper()
    
    def create_neutral_mob(self) -> Mob:
        return Mellstroy("Поляна")


# ==================== MobSpawner ====================
class MobSpawner:
    def __init__(self, factory: MobFactory):
        self.factory = factory
        self.biome_name = factory.__class__.__name__.replace("MobFactory", "")
    
    def spawn_hostile_mob(self) -> Mob:
        """Создать враждебного моба"""
        print(f"Спаун враждебного моба в биоме {self.biome_name}...")
        return self.factory.create_hostile_mob()
    
    def spawn_neutral_mob(self) -> Mob:
        """Создать нейтрального моба"""
        print(f"Спаун нейтрального моба в биоме {self.biome_name}...")
        return self.factory.create_neutral_mob()
    



# ==================== Основной код ====================
def main():
    print("МАЙКРАФТ: СИСТЕМА СОЗДАНИЯ МОБОВ")
    
    # Создаем фабрики для разных биомов
    forest_factory = ForestMobFactory()
    meadow_factory = MeadowMobFactory()
    
    print("СОЗДАНИЕ МОБОВ ЧЕРЕЗ ЛЕСНУЮ ФАБРИКУ")
    
    # Демонстрируем мобов из леса
    forest_spawner = MobSpawner(forest_factory)
    skelet=forest_spawner.spawn_hostile_mob()
    print(f"\nСоздан Скелет: {skelet.display()}")
    print(f"Скелет говорит говорит: {skelet.make_sound()}")
    print(f"Скелет атакует: {skelet.attack()}")
    
    print("СОЗДАНИЕ МОБОВ ЧЕРЕЗ ФАБРИКУ ПОЛЯНЫ")
    
    # Демонстрируем мобов с поляны
    meadow_spawner = MobSpawner(meadow_factory)
    Mellstroy=meadow_spawner.spawn_neutral_mob()
    
   
    print(f"\nСоздан Мелстрой: {Mellstroy.display()}")
    print(f"Мелстрой говорит говорит: {Mellstroy.make_sound()}")
    print(f"Мелстрой атакует: {Mellstroy.attack()}")
    crunpel=meadow_spawner.spawn_hostile_mob()
    
    print(f"\nСоздан Крюнпель: {crunpel.display()}")
    print(f"Крюнпель говорит говорит: {crunpel.make_sound()}")
    print(f"Крюнпель атакует: {crunpel.attack()}")

if __name__ == "__main__":
    main()
