 self.activities = activities
    
    def initialize_me(self):
        activity_list = AcitivyList([])
        with open('activities.json', 'r') as f:
            data = json.load(f)
            activity_list = AcitivyList(
                activities = self.get_activities_from_json(data)
            )
        return activity_list
    
    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name = activity['name'],
                    time_entries = self.get_time_entires_from_json(activity),
                )
            )
        self.activities = return_list
        return return_list
    
  
        
    def get_time_entires_from_json(self, data):
        return_list = []
        for entry in data['time_entries']:
            return_list.append(
                TimeEntry(
                    start_time = parser.parse(entry['start_time']),
                    end_time = parser.parse(entry['end_time']),
                    hours = entry['hours'],
                    minutes = entry['minutes'],
                    seconds = entry['seconds'],
                    keys=entry['keys']
                )
            )
        self.time_entries = return_list
        return return_list
    
    def serialize(self):
        return {
            'activities' : self.activities_to_json()
        }
    
    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())
        
        return activities_


class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name' : self.name,
            'time_entries' : self.make_time_entires_to_json()
        }
    
    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list


class TimeEntry:
    def __init__(self, start_time, end_time, hours, minutes, seconds, count_end,count_start):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.totalkeys=count_end-count_start
        self.count_start=count_end
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    
    def _get_specific_times(self):
        self.seconds =  self.total_time.seconds
        self.hours = self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60
        self.keys=self.totalkeys

    def serialize(self):
        return {
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds,
            'keys':self.keys
             }

        count = 0
        keyz = []
        
        def on_press(keyz):
            global keysz, count
            
            keysz.append(keyz)
            count += 1
            print(count)
            print("{0} pressed".format(keyz))
                                              
        def on_release(keyz):
            if keyz == Keyz.esc:
                return False
           
        
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        
        keys=count
        return keys

       
