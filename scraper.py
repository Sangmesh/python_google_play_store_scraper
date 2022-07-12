import play_store
print(play_store.details('com.android.chrome'))
print(play_store.categories())
print(play_store.search('chrome', page=2))