class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
        self.fleet_drop_speed=10
        self.ship_limit = 3
        

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
        self.bullet_width = 300
        
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        if self.bullet_width>=4.5:
            self.bullet_width //=1.5
        #print(self.bullet_width)
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

        

        